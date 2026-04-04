# ============================================================================
# AI-PMS RAG Bootcamp — LLM Fallback Chain Implementation
# 
# Purpose: Retry logic that cycles through free API providers
# when one hits rate limits or fails
# ============================================================================

import time
import logging
from typing import Tuple, Optional, Dict, List
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from openai import OpenAI, RateLimitError, APIError, APIConnectionError
try:
    import google.generativeai as genai
except ImportError:
    genai = None

from config.api_config import get_config

logger = logging.getLogger(__name__)

config = get_config()


# ============================================================================
# FALLBACK CHAIN CLASS
# ============================================================================

class LLMFallbackChain:
    """
    Manages fallback between multiple free LLM providers.
    
    Priority order:
    1. Groq (30 req/min, fastest)
    2. OpenRouter (backup, multiple free models)
    3. Cerebras (backup, fast)
    4. Google (fallback, different API style)
    """
    
    def __init__(self):
        """Initialize fallback chain with all configured providers"""
        self.config = config
        self.provider_history = []  # Track which provider was used
        
        # Build provider list based on configuration
        self.providers = self._build_provider_list()
        
        logger.info(f"Initialized fallback chain with {len(self.providers)} providers: {', '.join(self.providers.keys())}")
    
    def _build_provider_list(self) -> Dict:
        """Build dictionary of configured providers
        
        Returns:
            Dict mapping provider name to configuration
        """
        providers = {}
        
        # Groq (primary)
        if self.config.groq.is_configured():
            providers["groq"] = {
                "type": "openai-compatible",
                "config": self.config.groq,
                "description": "Groq (Llama 3.3 70B)"
            }
        
        # OpenRouter (backup)
        if self.config.openrouter.is_configured():
            providers["openrouter"] = {
                "type": "openai-compatible",
                "config": self.config.openrouter,
                "description": "OpenRouter (DeepSeek free)"
            }
        
        # Cerebras (backup)
        if self.config.cerebras.is_configured():
            providers["cerebras"] = {
                "type": "openai-compatible",
                "config": self.config.cerebras,
                "description": "Cerebras (Llama 3.3 70B)"
            }
        
        # Google (last resort, different API)
        if self.config.google.is_configured():
            providers["google"] = {
                "type": "google",
                "config": self.config.google,
                "description": "Google Gemini (1M token context!)"
            }
        
        return providers
    
    def query_openai_compatible(self, messages: List[Dict], provider_name: str, max_tokens: int = 1024) -> Tuple[str, str]:
        """Query an OpenAI-compatible provider (Groq, OpenRouter, Cerebras)
        
        Args:
            messages: Chat messages in OpenAI format
            provider_name: Name of provider (groq, openrouter, cerebras)
            max_tokens: Max tokens in response
        
        Returns:
            Tuple of (response_text, provider_name)
        
        Raises:
            APIError: If request fails
        """
        provider_info = self.providers[provider_name]
        cfg = provider_info["config"]
        
        try:
            logger.debug(f"Trying {provider_name}...")
            
            client = OpenAI(
                base_url=cfg.base_url,
                api_key=cfg.api_key
            )
            
            response = client.chat.completions.create(
                model=cfg.model,
                messages=messages,
                temperature=0.1,
                max_tokens=max_tokens
            )
            
            answer = response.choices[0].message.content
            logger.info(f"✓ {provider_name} succeeded")
            return answer, provider_name
            
        except RateLimitError as e:
            logger.warning(f"✗ {provider_name} rate limited (429): {e}")
            raise RateLimitError("Rate limit hit") from e
        
        except (APIConnectionError, APIError) as e:
            logger.warning(f"✗ {provider_name} failed: {e}")
            raise APIError("API error") from e
    
    def query_google(self, messages: List[Dict], max_tokens: int = 1024) -> Tuple[str, str]:
        """Query Google Gemini API (different interface)
        
        Args:
            messages: Chat messages
            max_tokens: Max tokens in response
        
        Returns:
            Tuple of (response_text, "google")
        
        Raises:
            Exception: If request fails
        """
        if not genai:
            raise ImportError("google-generativeai not installed. pip install google-generativeai")
        
        cfg = self.config.google
        
        try:
            logger.debug("Trying Google Gemini...")
            
            genai.configure(api_key=cfg.api_key)
            model = genai.GenerativeModel(cfg.model)
            
            # Convert OpenAI-style messages to Google format
            contents = messages[-1]["content"] if messages else ""
            
            response = model.generate_content(contents)
            
            answer = response.text
            logger.info("✓ Google Gemini succeeded")
            return answer, "google"
            
        except Exception as e:
            logger.warning(f"✗ Google Gemini failed: {e}")
            raise
    
    def query_llm(
        self,
        messages: List[Dict],
        max_tokens: int = 1024,
        provider_order: Optional[List[str]] = None,
        retry_delay: float = 1.0
    ) -> Tuple[str, str]:
        """
        Query LLM with fallback chain.
        
        Tries providers in order. On 429 (rate limit), waits and retries.
        On other errors, moves to next provider.
        
        Args:
            messages: Chat messages in OpenAI format
            max_tokens: Max tokens in response
            provider_order: Specific order to try (default: config.llm_fallback_order)
            retry_delay: Seconds to wait before retrying
        
        Returns:
            Tuple of (response_text, provider_used)
        
        Raises:
            Exception: If all providers fail
        """
        if not provider_order:
            provider_order = self.config.get_llm_fallback_order()
        
        if not provider_order:
            raise Exception("No LLM providers configured!")
        
        logger.info(f"Fallback chain: {' → '.join(provider_order)}")
        
        last_error = None
        
        for provider_name in provider_order:
            if provider_name not in self.providers:
                logger.warning(f"Provider {provider_name} not configured, skipping")
                continue
            
            try:
                provider_info = self.providers[provider_name]
                
                if provider_info["type"] == "openai-compatible":
                    # Handle rate limit by waiting and retrying
                    max_retries = 3
                    for attempt in range(max_retries):
                        try:
                            answer, used_provider = self.query_openai_compatible(
                                messages, provider_name, max_tokens
                            )
                            
                            # Track provider usage
                            self.provider_history.append({
                                "provider": used_provider,
                                "timestamp": time.time(),
                                "success": True
                            })
                            
                            return answer, used_provider
                            
                        except RateLimitError:
                            if attempt < max_retries - 1:
                                wait_time = retry_delay * (2 ** attempt)  # Exponential backoff
                                logger.info(f"Rate limited. Waiting {wait_time}s before retry...")
                                time.sleep(wait_time)
                            else:
                                logger.warning(f"{provider_name} rate limited after {max_retries} attempts")
                                last_error = f"{provider_name} rate limited"
                                raise
                
                elif provider_info["type"] == "google":
                    answer, used_provider = self.query_google(messages, max_tokens)
                    
                    # Track provider usage
                    self.provider_history.append({
                        "provider": used_provider,
                        "timestamp": time.time(),
                        "success": True
                    })
                    
                    return answer, used_provider
                    
            except Exception as e:
                last_error = str(e)
                logger.warning(f"Fallback: {provider_name} failed, trying next...")
                continue
        
        # All providers failed
        error_msg = f"All LLM providers failed. Last error: {last_error}"
        logger.error(f"✗ {error_msg}")
        
        # Track failure
        self.provider_history.append({
            "provider": "all_failed",
            "timestamp": time.time(),
            "success": False,
            "error": last_error
        })
        
        raise Exception(error_msg)
    
    def get_provider_stats(self) -> Dict:
        """Get statistics on provider usage
        
        Returns:
            Dict with provider usage stats
        """
        stats = {}
        for entry in self.provider_history:
            provider = entry["provider"]
            if provider not in stats:
                stats[provider] = {"success": 0, "failure": 0}
            
            if entry["success"]:
                stats[provider]["success"] += 1
            else:
                stats[provider]["failure"] += 1
        
        return stats
    
    def log_provider_stats(self):
        """Log provider usage statistics"""
        stats = self.get_provider_stats()
        logger.info("Provider Usage Statistics:")
        for provider, counts in stats.items():
            total = counts["success"] + counts["failure"]
            success_rate = (counts["success"] / total * 100) if total > 0 else 0
            logger.info(f"  {provider:15} {counts['success']:3} success / {counts['failure']:3} failure ({success_rate:5.1f}%)")


# ============================================================================
# SINGLETON INSTANCE
# ============================================================================

# Global fallback chain instance
_fallback_chain: Optional[LLMFallbackChain] = None


def get_fallback_chain() -> LLMFallbackChain:
    """Get or create the global fallback chain instance"""
    global _fallback_chain
    if _fallback_chain is None:
        _fallback_chain = LLMFallbackChain()
    return _fallback_chain


# ============================================================================
# CONVENIENCE FUNCTION
# ============================================================================

def query_llm(
    messages: List[Dict],
    max_tokens: int = 1024,
    provider_order: Optional[List[str]] = None
) -> Tuple[str, str]:
    """
    Convenience function to query LLM with fallback.
    
    Usage:
        from scripts.fallback_chain import query_llm
        
        answer, provider = query_llm([
            {"role": "user", "content": "What is RAGAS?"}
        ])
        print(f"Answer from {provider}: {answer}")
    
    Args:
        messages: Chat messages in OpenAI format
        max_tokens: Max tokens in response
        provider_order: Specific provider order
    
    Returns:
        Tuple of (answer_text, provider_name)
    """
    chain = get_fallback_chain()
    return chain.query_llm(messages, max_tokens, provider_order)


# ============================================================================
# EXAMPLE USAGE & TESTING
# ============================================================================

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("\n" + "=" * 70)
    print("LLM Fallback Chain Test")
    print("=" * 70 + "\n")
    
    chain = get_fallback_chain()
    
    print("Configured Providers:")
    for provider, info in chain.providers.items():
        print(f"  ✓ {provider:15} {info['description']}")
    
    print("\n" + "-" * 70)
    print("Testing Query with Fallback Chain...")
    print("-" * 70 + "\n")
    
    try:
        messages = [
            {
                "role": "user",
                "content": "What is RAG (Retrieval-Augmented Generation) in simple terms?"
            }
        ]
        
        answer, provider = query_llm(messages, max_tokens=256)
        
        print(f"\n✓ Success!")
        print(f"Provider Used: {provider}")
        print(f"\nAnswer:\n{answer}")
        
        print("\n" + "-" * 70)
        chain.log_provider_stats()
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nMake sure your .env file is configured with at least one API key.")
