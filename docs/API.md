# API Reference Documentation

This document provides a reference for the REST API endpoints exposed by the AI-PMS RAG Bootcamp application.

> **Note:** When the application is running, you can access the interactive Swagger UI at `http://localhost:8000/docs`.

## Base URL
All API requests should be prefixed with the base URL (e.g., `http://localhost:8000`).

---

## Authentication
Most endpoints require an API Key passed in the header.
- **Header:** `X-API-Key`
- **Value:** Your designated API key (e.g., `super_secret_key_123`)

---

## Endpoints

### 1. Execute Query
Runs a production-hardened RAG query against the database, utilizing LangGraph, RLS isolation, and adversarial guardrails.

**Endpoint:** `POST /query`

**Headers:**
- `X-API-Key`: `<your_api_key>`
- `Content-Type`: `application/json`

**Request Body (JSON):**
| Field | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The user's search query (min 3 chars). |
| `tenant_id` | string | Yes | Tenant isolation identifier (default: "metro_tenant"). |
| `entity_type_filter` | string | No | Optional domain constraint (e.g., "contract_clause", "ncr", "dpr", "correspondence"). |

**Example Request:**
```json
{
  "query": "What are the safety requirements for the viaduct?",
  "tenant_id": "metro_tenant",
  "entity_type_filter": "contract_clause"
}
```

**Example Response (200 OK):**
```json
{
  "query": "What are the safety requirements for the viaduct?",
  "tenant_id": "metro_tenant",
  "answer": "The safety requirements mandate a 2.5m clearance...",
  "citations": "1. contract_docs (Page 12)\n2. viaduct_specs (Page 4)",
  "confidence": "high",
  "retrieval_trace": [
    { "action": "vector_search", "nodes_found": 5 }
  ],
  "latency_ms": 1245.5,
  "latency_status": "PASSED",
  "latency_budget_ms": 5000
}
```

### 2. Document Upload (Placeholder)
Uploads a document to be ingested, chunked, and vectorized for a specific tenant.

**Endpoint:** `POST /documents/upload`

**Headers:**
- `X-API-Key`: `<your_api_key>`
- `Content-Type`: `multipart/form-data`

**Form Data:**
- `file`: The document file (e.g., `.pdf`, `.txt`, `.xlsx`)
- `tenant_id`: The tenant ID string.

**Example Response (200 OK):**
```json
{
  "status": "success",
  "message": "Document ingested successfully",
  "chunks_created": 42
}
```

---

## Rate Limiting
The API enforces rate limits to prevent abuse:
- **Per IP:** 10 requests per minute.
- **Per Tenant:** 50 requests per minute.

If a rate limit is exceeded, a `429 Too Many Requests` error is returned.
