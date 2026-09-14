# Phase 5 — System Architecture

## 1. Architecture Objective

DecisionOS is designed as an evidence-backed AI decision-support system for critical electronic component sourcing.

The architecture must support:

* Evidence traceability
* Deterministic decision scoring
* AI-assisted research and interpretation
* Counter-evidence analysis
* Sensitivity analysis
* Recommendation stability analysis
* Human review and override
* Reproducible decisions
* Clear separation between AI reasoning and business logic

The central architectural principle is:

> **LLMs interpret evidence. Deterministic software makes decisions reproducible. Humans make the final decision.**

---

## 2. High-Level Architecture

DecisionOS consists of the following logical layers:

```text
┌──────────────────────────────────────────────┐
│                 Web Application              │
│              Next.js + TypeScript            │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                    API Layer                 │
│                  FastAPI + Python            │
└──────────────────────┬───────────────────────┘
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Decision     │ │ Research &   │ │ Evaluation   │
│ Engine       │ │ Retrieval    │ │ Services     │
└──────┬───────┘ └──────┬───────┘ └──────────────┘
       │                 │
       │                 ▼
       │        ┌──────────────────┐
       │        │  Evidence Layer  │
       │        └────────┬─────────┘
       │                 │
       └────────┬────────┘
                ▼
┌──────────────────────────────────────────────┐
│                 Data Layer                   │
│          PostgreSQL + pgvector               │
└──────────────────────────────────────────────┘

External Data Sources
        │
        ▼
Manufacturer Sites / Distributors / Public Sources
```

---

## 3. Technology Stack

### Frontend

* Next.js
* TypeScript
* React
* App Router
* Component-based UI

The frontend provides the product interface for decision creation, requirements management, evidence review, supplier comparison, recommendations, and human decision recording.

### Backend

* Python
* FastAPI
* Pydantic
* Python-based decision and evaluation logic

FastAPI provides the API boundary between the frontend and backend services.

### Database

* PostgreSQL
* pgvector

PostgreSQL is the primary system of record.

Vector search is used where semantic retrieval is useful, but vector similarity is not treated as the source of truth for numerical procurement decisions.

### AI Layer

* Large Language Model API
* Embedding model
* Retrieval and extraction pipeline

The AI layer assists with:

* Research
* Information extraction
* Claim generation
* Evidence classification
* Evidence interpretation
* Counter-evidence discovery
* Recommendation explanation

The AI layer does not own deterministic sco

