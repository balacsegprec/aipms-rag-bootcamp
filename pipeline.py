from llm_engine import generate_response
from config import Config


def pipeline(user_query):

    Config.validate()

    # 1. preprocess
    query = user_query.strip()

    # 2. retrieval (dummy for now)
    context = "AI is a branch of computer science that focuses on intelligent machines."

    # 3. prompt building
    prompt = f"""
    Use the context to answer:

    Context:
    {context}

    Question:
    {query}
    """

    # 4. LLM with fallback
    answer = generate_response(prompt)

    # 5. postprocess
    return answer.strip()


if __name__ == "__main__":
    print(pipeline("Explain artificial intelligence"))