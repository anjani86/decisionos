# DecisionOS

> Evidence-backed AI decision intelligence for procurement and supplier selection.

DecisionOS is a portfolio project exploring how AI can help procurement teams make **transparent, evidence-backed, and defensible supplier decisions**.

The system combines evidence, criterion assessments, hard constraints, deterministic scoring, comparison, sensitivity analysis, and stability analysis into a structured decision workflow.

The core principle is:

> **AI recommends. Humans decide.**

---

## Problem

Supplier selection involves multiple competing factors:

* Technical fit
* Availability
* Lead time
* Price
* Product lifecycle
* Supply risk
* Geographic risk
* Compliance

The challenge is not simply finding information.

The challenge is turning that information into a decision that can answer:

> **Why is this supplier recommended, what evidence supports the recommendation, what evidence challenges it, and how sensitive is the decision to changing assumptions?**

DecisionOS explores a structured approach to this problem.

---

## Initial Use Case

### Electronic Component Supplier Selection

The first use case is procurement of electronic components.

A procurement team may need to compare suppliers while enforcing requirements such as:

* Maximum lead time
* Maximum price
* RoHS compliance
* Required lifecycle status

At the same time, suppliers can be evaluated using weighted criteria such as:

* Technical fit
* Availability
* Lead time
* Price
* Lifecycle
* Supply risk
* Geographic risk

DecisionOS separates **hard constraints** from **weighted criteria**.

A supplier that violates a mandatory requirement should not be rescued simply because it has a high overall score.

---

## Decision Flow

```text
Requirements
     |
     v
Evidence
     |
     v
Criterion Assessment
     |
     +------------------+
     |                  |
     v                  v
Supporting         Counter-Evidence
Evidence
     |                  |
     +--------+---------+
              |
              v
       Hard Constraints
              |
              v
       Decision Engine
              |
       +------+------+
       |             |
       v             v
     Score          Risk
       |             |
       +------+------+
              |
              v
   Sensitivity / Stability
              |
              v
       Recommendation
              |
              v
        Human Decision
```

---

# Core Capabilities

## Evidence Model

Evidence is represented explicitly rather than treating an AI response as the evidence itself.

Each evidence item contains:

* Source name
* Source URL
* Claim
* Evidence type
* Confidence

Supported evidence types:

* `supporting`
* `contradicting`
* `neutral`
* `missing`

---

## Criterion Assessment

Evidence can be organized into criterion-level assessments.

Each assessment contains:

* Criterion
* Assessment
* Score
* Confidence
* Supporting evidence
* Counter-evidence

The system also identifies whether evidence is:

* Supporting
* Conflicting
* Insufficient

---

## Hard Constraints

DecisionOS distinguishes mandatory requirements from weighted decision criteria.

Example:

```text
Maximum lead time: 12 weeks
Maximum price:     $15
RoHS required:     Yes
Lifecycle:         Active
```

If a supplier violates a hard constraint, the option can become ineligible regardless of its weighted score.

Example:

```text
Supplier B

Lead time: 16 weeks
Maximum allowed: 12 weeks

Result: INELIGIBLE
```

---

## Deterministic Decision Engine

The current decision engine uses explicit weighted criteria.

Default weights:

| Criterion       | Weight |
| --------------- | -----: |
| Technical Fit   |   0.25 |
| Availability    |   0.20 |
| Lead Time       |   0.15 |
| Price           |   0.15 |
| Lifecycle       |   0.10 |
| Supply Risk     |   0.10 |
| Geographic Risk |   0.05 |

Weighted contribution is calculated as:

```text
criterion score × criterion weight
```

Current recommendation thresholds:

```text
80+  → recommended
60–79.99 → acceptable
<60  → not_recommended
```

Hard constraint failures are handled separately from the weighted score.

---

## Supplier Comparison

Multiple supplier options can be evaluated using the same criteria.

The comparison capability helps expose:

* Overall score differences
* Criterion-level differences
* Constraint failures
* Trade-offs between suppliers

---

## Counter-Evidence

DecisionOS explicitly supports evidence that challenges an assessment.

Example:

```text
Supporting evidence:
Product is listed as active.

Counter-evidence:
Other information indicates potential supply constraints.
```

The purpose is to make conflicting information visible instead of hiding it behind a single conclusion.

---

## Sensitivity Analysis

DecisionOS can examine how the recommendation changes when decision inputs change.

This helps answer:

> How dependent is the recommendation on the current assumptions?

---

## Stability Analysis

DecisionOS can also examine how recommendation status changes as the decision score changes.

For example:

```text
92 → recommended
87 → recommended
82 → recommended
77 → acceptable
```

This helps identify recommendations that are close to a decision boundary.

---

# API

DecisionOS currently provides a FastAPI backend.

| Method | Endpoint           | Purpose                     |
| ------ | ------------------ | --------------------------- |
| GET    | `/health`          | Health check                |
| POST   | `/research`        | Research workflow           |
| POST   | `/evidence`        | Evidence processing         |
| POST   | `/assessment`      | Criterion assessment        |
| POST   | `/decision`        | Decision evaluation         |
| POST   | `/comparison`      | Supplier comparison         |
| POST   | `/sensitivity`     | Sensitivity analysis        |
| POST   | `/stability`       | Stability analysis          |
| POST   | `/source/retrieve` | Source retrieval contract   |
| POST   | `/source/evidence` | Source-to-evidence workflow |

Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# Example Decision

A simplified decision can evaluate a supplier using weighted criteria and hard constraints.

```json
{
  "option_name": "STM32F407VGT6 - Supplier A",
  "criteria": [
    {
      "name": "Technical Fit",
      "weight": 0.25,
      "score": 90
    },
    {
      "name": "Availability",
      "weight": 0.20,
      "score": 90
    },
    {
      "name": "Lead Time",
      "weight": 0.15,
      "score": 95
    },
    {
      "name": "Price",
      "weight": 0.15,
      "score": 85
    },
    {
      "name": "Lifecycle",
      "weight": 0.10,
      "score": 95
    },
    {
      "name": "Supply Risk",
      "weight": 0.10,
      "score": 90
    },
    {
      "name": "Geographic Risk",
      "weight": 0.05,
      "score": 90
    }
  ],
  "lead_time_weeks": 8,
  "price": 10,
  "rohs_compliant": true,
  "lifecycle_status": "active"
}
```

---

# Technology

* Python 3.12
* FastAPI
* Pydantic
* Pytest
* REST API
* OpenAPI / Swagger
* Deterministic Python decision logic

The decision layer is intentionally deterministic and testable.

---

# Project Structure

```text
decisionos/
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── decision.py
│       ├── evidence.py
│       └── research.py
│
├── docs/
│   ├── 01-product-discovery.md
│   ├── 02-market-research.md
│   ├── 03-data-strategy.md
│   ├── 04-product-requirements.md
│   └── 05-system-architecture.md
│
├── tests/
│   └── ...
│
└── README.md
```

---

# Documentation

The `/docs` directory contains the product and technical thinking behind DecisionOS:

* Product discovery
* Market research
* Data strategy
* Product requirements
* System architecture

The project is intended to demonstrate both **product thinking and engineering execution**.

---

# Run Locally

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the tests:

```bash
PYTHONPATH=backend pytest -q
```

Start the API:

```bash
PYTHONPATH=backend uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "decisionos-api",
  "version": "0.1.0"
}
```

---

# Testing

The test suite covers:

* Decision scoring
* Weighted criteria
* Hard constraints
* Evidence models
* Counter-evidence
* Criterion assessments
* Assessment-to-decision transformation
* Supplier comparison
* Sensitivity analysis
* Stability analysis
* API behavior
* Source retrieval contracts

Current test status:

```text
30 passed
1 warning
```

The warning is from a dependency deprecation and does not represent a failing test.

---

# Current Status

| Capability                          | Status      |
| ----------------------------------- | ----------- |
| Product hypothesis                  | Implemented |
| Procurement use case                | Defined     |
| Product discovery                   | Documented  |
| Market research                     | Documented  |
| Data strategy                       | Documented  |
| Product requirements                | Documented  |
| System architecture                 | Documented  |
| Evidence model                      | Implemented |
| Criterion assessments               | Implemented |
| Hard constraints                    | Implemented |
| Decision engine                     | Implemented |
| Supplier comparison                 | Implemented |
| Sensitivity analysis                | Implemented |
| Stability analysis                  | Implemented |
| Automated tests                     | Implemented |
| FastAPI API                         | Implemented |
| Source retrieval contract           | Implemented |
| Production-grade external retrieval | In progress |
| Web application                     | Future      |
| Evaluation benchmark                | Future      |
| Deployment                          | Future      |

---

# Current Limitation

The source retrieval capability currently provides the retrieval contract and implementation, but external websites may not always be reliably accessible from a local Python HTTP client.

This can happen because of:

* Redirect behavior
* Bot protection
* Network restrictions
* Website-specific security policies

The core DecisionOS decision engine does not depend on successful live retrieval from a particular external website.

The retrieval layer is therefore being treated as an integration area that will be hardened separately.

---

# Evaluation

Future evaluation will measure the quality of the decision-intelligence pipeline.

Planned dimensions include:

* Evidence retrieval accuracy
* Claim-to-source accuracy
* Citation correctness
* Contradiction detection
* Assessment consistency
* Decision consistency
* Recommendation stability
* Hallucination rate
* Latency
* Cost

---

# Roadmap

## Completed

* Product hypothesis
* Initial procurement use case
* Product discovery
* Market research
* Data strategy
* Product requirements
* System architecture
* Evidence model
* Criterion assessment model
* Hard constraints
* Decision engine
* Supplier comparison
* Sensitivity analysis
* Stability analysis
* Automated tests
* FastAPI backend

## In Progress

* End-to-end procurement demonstration
* Source retrieval hardening
* Evaluation benchmark
* Evidence retrieval pipeline

## Future

* Web application
* LLM-assisted research
* Automated contradiction detection
* Supplier data integrations
* Production deployment
* Evaluation dashboard

---

# Product Principle

> **AI recommends. Humans decide.**

DecisionOS is designed to make the evidence, assumptions, constraints, trade-offs, and uncertainty behind a decision easier to inspect.

The goal is not to replace procurement judgment.

The goal is to support better-informed human decisions.

---

# Why This Project?

DecisionOS explores a broader product question:

> **How can AI help people make better decisions when information is fragmented, uncertain, and contradictory?**

Procurement is the initial domain because supplier selection combines:

* Structured criteria
* External evidence
* Hard constraints
* Uncertainty
* Trade-offs
* Business consequences

The same decision-intelligence principles can potentially be applied to other complex business decisions where evidence and explainability matter.

---

# Portfolio Context

DecisionOS is an independent portfolio project combining:

* Product discovery
* AI product design
* Backend engineering
* Decision-system design
* Evidence modeling
* API development
* Automated testing
* System architecture

The project is intentionally built as a practical implementation rather than a conceptual AI demo.

---

# Disclaimer

DecisionOS is an independent portfolio project and research prototype.

It is not intended to provide professional procurement, financial, legal, compliance, or supply-chain advice.

---

# License

MIT
