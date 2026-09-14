# Phase 5 — System Architecture

## 1. Architecture Objective

DecisionOS is an evidence-backed AI decision-support system for critical electronic component sourcing.

The architecture is designed around:

* Evidence traceability
* Deterministic decision scoring
* AI-assisted research and interpretation
* Counter-evidence analysis
* Sensitivity analysis
* Recommendation stability
* Human review and override
* Reproducible decisions
* Clear separation between AI reasoning and business logic

The central principle is:

> **LLMs interpret evidence. Deterministic software makes decisions reproducible. Humans make the final decision.**

---

## 2. High-Level Architecture

```text
┌──────────────────────────────────────┐
│              User                    │
│       Procurement Manager            │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│        Next.js + TypeScript           │
│          Decision Interface           │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          FastAPI + Python             │
│              API Layer                │
└──────────────────┬───────────────────┘
                   │
       ┌───────────┼────────────┐
       ▼           ▼            ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│  Decision  │ │ Research & │ │ Evaluation │
│   Engine   │ │ Retrieval  │ │  Services  │
└─────┬──────┘ └──────┬─────┘ └────────────┘
      │               │
      │               ▼
      │       ┌────────────────┐
      │       │ Evidence Layer │
      │       └───────┬────────┘
      │               │
      └───────┬───────┘
              ▼
┌──────────────────────────────────────┐
│       PostgreSQL + pgvector           │
│           Data Layer                  │
└──────────────────────────────────────┘
              ▲
              │
┌─────────────┴────────────────────────┐
│ Manufacturer / Distributor / Public  │
│              Sources                 │
└──────────────────────────────────────┘
```

---

# 3. Technology Stack

## Frontend

* Next.js
* TypeScript
* React
* App Router

The frontend provides:

* Decision creation
* Requirement configuration
* Candidate comparison
* Evidence review
* Recommendation review
* Counter-evidence interaction
* Sensitivity analysis
* Human decision recording

## Backend

* Python
* FastAPI
* Pydantic

The backend provides:

* API endpoints
* Decision management
* Research orchestration
* Evidence processing
* Scoring
* Recommendation generation
* Sensitivity analysis
* Evaluation services

## Database

* PostgreSQL
* pgvector

PostgreSQL is the authoritative system of record.

pgvector supports semantic retrieval where useful, but vector similarity is not treated as the source of truth for numerical decisions.

## AI Layer

The AI layer consists of:

* LLM API
* Embedding model
* Retrieval pipeline
* Evidence extraction pipeline

AI is used for interpretation and research assistance, not deterministic business calculations.

---

# 4. Core Components

## 4.1 Web Application

The web application allows users to:

1. Create a procurement decision
2. Define requirements
3. Define hard constraints
4. Configure weighted criteria
5. Add candidate sourcing options
6. Review research evidence
7. Compare candidates
8. Review recommendations
9. Challenge recommendations
10. Run sensitivity analysis
11. Record the final human decision

The interface should expose the reasoning behind a recommendation rather than presenting an unexplained AI answer.

---

## 4.2 API Layer

The API layer connects the frontend to backend services.

Responsibilities:

* Request validation
* Decision management
* Candidate management
* Research requests
* Evidence retrieval
* Evaluation requests
* Recommendation requests
* Sensitivity analysis
* Human decision recording

The API layer should remain relatively thin.

Business logic belongs in dedicated services.

---

## 4.3 Decision Service

The Decision Service manages the lifecycle of a procurement decision.

Responsibilities:

* Create decisions
* Store requirements
* Store constraints
* Store criteria
* Store candidate options
* Retrieve decision state
* Update decision state
* Record human decisions

A decision represents a specific procurement question at a specific point in time.

---

# 5. Research & Retrieval Service

The Research & Retrieval Service gathers relevant information from external sources.

Responsibilities:

* Generate research questions
* Search external sources
* Retrieve source content
* Identify relevant passages
* Extract structured claims
* Capture source metadata
* Record retrieval time
* Associate evidence with candidates and criteria

Preferred sources include:

* Component manufacturer websites
* Authorized distributors
* Official datasheets
* Supplier documentation
* Public company information
* Relevant public supply-chain sources

The research system should prioritize authoritative and current sources.

---

# 6. Evidence Layer

The Evidence Layer is the core trust mechanism of DecisionOS.

The evidence chain is:

```text
Source
   ↓
Evidence
   ↓
Claim
   ↓
Criterion
   ↓
Assessment
   ↓
Score
   ↓
Recommendation
```

Important recommendation claims should be traceable through this chain.

An evidence record may contain:

* Source
* Source title
* Source URL
* Retrieval date
* Evidence text
* Related sourcing option
* Related criterion
* Evidence type
* Confidence
* Freshness

Evidence types:

* Supporting
* Contradicting
* Neutral
* Missing

---

# 7. LLM Boundary

The LLM is an analytical component.

It is not the system of record and does not control deterministic decision logic.

## LLM Responsibilities

The LLM may:

* Summarize source information
* Extract structured claims
* Interpret technical information
* Classify evidence
* Identify relevant criteria
* Generate research questions
* Discover counter-evidence
* Explain recommendations
* Identify weaknesses in recommendations

## Deterministic Software Responsibilities

Application code must control:

* Hard constraint evaluation
* Numerical normalization
* Weighted scoring
* Score aggregation
* Eligibility determination
* Sensitivity calculations
* Recommendation stability
* Decision state
* Final decision recording

The LLM must not independently determine the final numerical score.

---

# 8. Decision Engine

The Decision Engine converts structured assessments into reproducible outputs.

```text
Candidate Option
       ↓
Hard Constraint Check
       ↓
Eligibility
       ↓
Criterion Assessments
       ↓
Normalized Scores
       ↓
Weighted Scores
       ↓
Overall Score
       ↓
Risk Analysis
       ↓
Recommendation
```

## Hard Constraints

Hard constraints are mandatory eligibility conditions.

Examples:

* Lead time ≤ 12 weeks
* Annual capacity ≥ required demand
* RoHS compliance required
* Operating temperature requirement satisfied

If a sourcing option fails a mandatory constraint, it becomes:

**INELIGIBLE**

It should not simply receive a lower weighted score.

---

# 9. Scoring Model

Eligible sourcing options receive criterion-level scores.

Example:

| Criterion       | Weight |
| --------------- | -----: |
| Technical Fit   |    25% |
| Availability    |    20% |
| Lead Time       |    15% |
| Price           |    15% |
| Lifecycle       |    10% |
| Supply Risk     |    10% |
| Geographic Risk |     5% |

Weights must total 100%.

The system calculates:

```text
Overall Score =
Σ (Criterion Score × Criterion Weight)
```

The calculation must be deterministic.

Given identical:

* Requirements
* Candidate data
* Evidence assessments
* Criteria
* Weights

the system should produce the same numerical result.

---

# 10. Evidence Confidence

Evidence quality is represented separately from numerical scoring.

Confidence may consider:

* Source authority
* Evidence freshness
* Evidence completeness
* Agreement between sources
* Contradictory evidence
* Evidence specificity

Confidence levels:

* High
* Medium
* Low
* Unknown

Low confidence does not automatically mean a low supplier score.

It indicates uncertainty around the assessment.

---

# 11. Contradictory Evidence

DecisionOS must preserve conflicting information instead of silently choosing one source.

Example:

```text
Source A:
Lead time = 8 weeks

Source B:
Lead time = 20 weeks
```

The system should surface:

```text
Contradictory Evidence Detected

Assessment:
Lead-time information is inconsistent.

Confidence:
Low

Human verification recommended.
```

Contradictions remain visible in the evidence layer.

---

# 12. Counter-Evidence Engine

The Counter-Evidence Engine searches for information that could weaken the current recommendation.

Example:

```text
Recommendation:
Supplier A

Challenge:
What could make Supplier A the wrong choice?
```

The system searches for:

* Negative supplier signals
* Lifecycle concerns
* Availability deterioration
* Lead-time problems
* Quality concerns
* Geographic risks
* Conflicting technical information
* Stronger alternatives

Results are classified as:

* Supporting evidence
* Weakening evidence
* Missing evidence

The purpose is to reduce confirmation bias in AI-generated recommendations.

---

# 13. Sensitivity Analysis

The Sensitivity Analysis Engine tests whether the recommendation remains stable when important assumptions change.

Examples:

```text
Price Weight:
15% → 25%

Risk Weight:
10% → 20%

Maximum Lead Time:
12 weeks → 8 weeks

Annual Demand:
100,000 → 150,000 units
```

The system recalculates the decision using deterministic logic.

Results should show:

* Original recommendation
* New recommendation
* Score changes
* Ranking changes
* Assumption responsible for the change

---

# 14. Recommendation Stability

Recommendation stability describes how sensitive the result is to plausible changes in assumptions.

## High Stability

The recommended option remains first across reasonable changes.

## Medium Stability

The recommended option remains first under most scenarios but loses under several plausible scenarios.

## Low Stability

Small changes in assumptions cause the recommended option to change.

A recommendation should not be presented as highly certain when its ranking is unstable.

---

# 15. Recommendation Service

The Recommendation Service combines:

* Eligibility
* Weighted scores
* Evidence
* Confidence
* Risk signals
* Counter-evidence
* Sensitivity analysis
* Recommendation stability

A recommendation should contain:

```text
Recommended Option

Why it wins

Key strengths

Key weaknesses

Supporting evidence

Contradicting evidence

Confidence

Recommendation stability

What could change the decision

Recommended next action
```

The explanation must be traceable to underlying evidence and assessments.

---

# 16. Human Decision Layer

DecisionOS does not automatically award business to a supplier.

The workflow is:

```text
AI Analysis
     ↓
Recommendation
     ↓
Human Review
     ↓
Challenge
     ↓
Sensitivity Analysis
     ↓
Human Decision
```

The system records:

* Selected option
* Whether selection matches recommendation
* Decision status
* Human rationale
* Human notes
* Decision timestamp

The human decision is authoritative.

---

# 17. Data Model

The initial conceptual data model contains:

```text
Decision
 ├── Requirements
 ├── Constraints
 ├── Criteria
 ├── Sourcing Options
 │     ├── Component
 │     ├── Supplier
 │     └── Commercial Data
 │
 ├── Evidence
 │     ├── Sources
 │     ├── Claims
 │     └── Assessments
 │
 ├── Scores
 ├── Risk Signals
 ├── Recommendation
 ├── Sensitivity Results
 └── Human Decision
```

Primary entities:

* Decision
* Component
* Supplier
* SourcingOption
* Requirement
* Constraint
* Criterion
* Source
* Evidence
* Claim
* Assessment
* RiskSignal
* Score
* Recommendation
* SensitivityResult
* HumanDecision

---

# 18. Data Persistence

PostgreSQL is the authoritative data store.

Relational data should include:

* Decisions
* Components
* Suppliers
* Sourcing options
* Requirements
* Criteria
* Constraints
* Scores
* Evidence metadata
* Recommendations
* Human decisions

Vector embeddings may be stored for semantic retrieval.

Vector search is an auxiliary capability and is not the authoritative decision mechanism.

---

# 19. API Boundary

The initial API exposes product capabilities rather than implementation details.

Conceptual endpoints:

```text
POST   /decisions
GET    /decisions/{id}

POST   /decisions/{id}/requirements
POST   /decisions/{id}/constraints
POST   /decisions/{id}/criteria

POST   /decisions/{id}/options
GET    /decisions/{id}/options

POST   /decisions/{id}/research
GET    /decisions/{id}/evidence

POST   /decisions/{id}/evaluate
GET    /decisions/{id}/scores

POST   /decisions/{id}/recommendation
POST   /decisions/{id}/challenge
POST   /decisions/{id}/sensitivity

POST   /decisions/{id}/human-decision
```

The exact API contract may evolve during implementation.

---

# 20. Research Data Flow

```text
Decision Requirements
        ↓
Research Questions
        ↓
Search / Retrieval
        ↓
Source Documents
        ↓
Relevant Passages
        ↓
Structured Claims
        ↓
Evidence Classification
        ↓
Criterion Assessment
        ↓
Decision Engine
```

The system should preserve enough information to reconstruct how an important claim was derived from its source.

---

# 21. Recommendation Data Flow

```text
Decision
   ↓
Candidate Options
   ↓
Hard Constraint Evaluation
   ↓
Evidence Assessment
   ↓
Criterion Scores
   ↓
Weighted Scoring
   ↓
Risk Analysis
   ↓
Counter-Evidence
   ↓
Sensitivity Analysis
   ↓
Recommendation Stability
   ↓
Recommendation
   ↓
Human Decision
```

---

# 22. Evaluation Architecture

The architecture must allow AI components to be evaluated independently from the user interface.

## Retrieval Evaluation

Measure:

* Source relevance
* Evidence retrieval accuracy
* Citation correctness

## Extraction Evaluation

Measure:

* Claim extraction accuracy
* Criterion classification accuracy
* Evidence classification accuracy

## Decision Evaluation

Measure:

* Constraint correctness
* Score correctness
* Ranking correctness
* Sensitivity correctness

## Recommendation Evaluation

Measure:

* Evidence grounding
* Explanation quality
* Counter-evidence quality
* Recommendation stability

## Human Evaluation

Measure:

* Decision usefulness
* Trust
* Review effort
* Ability to identify uncertainty
* Ability to challenge the recommendation

---

# 23. Security and Data Protection

The system must:

* Keep API keys outside source control
* Store secrets using environment-based configuration
* Validate API inputs
* Restrict access to decision data
* Avoid exposing credentials through logs
* Treat retrieved external content as untrusted input
* Prevent external documents from directly controlling application behavior

External research content must be treated as data, not executable instructions.

---

# 24. Observability

Important system events should be observable.

Examples:

* Research request
* Source retrieval
* Evidence extraction
* Evidence classification
* Scoring execution
* Recommendation generation
* Counter-evidence search
* Sensitivity calculation
* Human decision

The system should make it possible to diagnose why a recommendation was produced.

---

# 25. Failure Handling

DecisionOS should fail conservatively.

## Research Failure

If external research cannot be retrieved:

```text
Evidence unavailable
```

The system should not invent replacement evidence.

## Conflicting Evidence

Surface the conflict and reduce confidence.

## Missing Data

Represent the value as unknown rather than guessing.

## LLM Failure

Preserve structured decision data and allow deterministic components to remain usable.

## Scoring Failure

Do not produce a recommendation from incomplete or invalid scoring inputs.

---

# 26. Architecture Principles

### Principle 1 — Evidence Before Recommendation

Recommendations must be grounded in evidence.

### Principle 2 — Deterministic Decisions

Numerical scoring and constraints must be reproducible.

### Principle 3 — AI Assists, Software Governs

LLMs interpret and analyze; application logic enforces decision rules.

### Principle 4 — Uncertainty Is Data

Missing and conflicting evidence must be represented explicitly.

### Principle 5 — Challenge Is a First-Class Capability

The system should actively test its own recommendation.

### Principle 6 — Human Authority

The AI recommendation never replaces the human procurement decision.

### Principle 7 — Traceability

Users should be able to move from recommendation back to the evidence supporting it.

### Principle 8 — Evaluation Is Part of the Architecture

AI components must be independently measurable.

---

# 27. Architecture Non-Goals

The initial architecture does not attempt to provide:

* ERP replacement
* Procurement marketplace
* Autonomous purchasing
* Supplier contracting
* Payment processing
* Automated purchase orders
* Full enterprise identity management
* Complete BOM lifecycle management
* Global real-time supply-chain simulation
* Autonomous procurement agents

The architecture remains focused on evidence-backed decision intelligence.

---

# 28. Target Architecture

```text
                    USER
                     │
                     ▼
          ┌──────────────────────┐
          │       Next.js        │
          │    Decision UI       │
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │       FastAPI        │
          │      API Layer       │
          └──────────┬───────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
 ┌────────────┐ ┌────────────┐ ┌────────────┐
 │  Decision  │ │ Research & │ │ Evaluation │
 │   Engine   │ │ Retrieval  │ │  Services  │
 └─────┬──────┘ └──────┬─────┘ └────────────┘
       │               │
       │               ▼
       │       ┌────────────────┐
       │       │ Evidence Layer │
       │       └───────┬────────┘
       │               │
       └───────┬───────┘
               ▼
      ┌────────────────────┐
      │    PostgreSQL      │
      │    + pgvector      │
      └─────────┬──────────┘
                │
                ▼
      External Data Sources

              AI Layer
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
 LLM Interpretation   Semantic Retrieval
       │                   │
       └─────────┬─────────┘
                 ▼
           Evidence Layer
                 │
                 ▼
          Human Decision
```

---

# 29. Architectural Principle

The defining architecture of DecisionOS is:

> **Research produces evidence. Evidence informs assessments. Assessments feed deterministic decision logic. AI explains and challenges the result. Humans make the final decision.**

This separation is fundamental to making DecisionOS explainable, reproducible, evaluable, and trustworthy.
