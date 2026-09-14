# DecisionOS

> **Evidence-backed AI decision intelligence for supplier selection and procurement.**

DecisionOS is an early-stage AI product exploring how procurement teams can make faster, more transparent, and more defensible supplier-selection decisions when relevant information is fragmented across financial data, company information, certifications, market signals, news, and other sources.

## The Problem

Supplier selection is a multi-dimensional decision.

Procurement teams may need to evaluate:

* Cost
* Technical fit
* Quality and certifications
* Delivery reliability
* Capacity
* Financial stability
* Geographic and geopolitical risk
* Compliance
* Supplier concentration
* Strategic fit

The challenge is not simply finding information.

The challenge is turning fragmented and sometimes contradictory information into a decision that a procurement professional can understand, challenge, and defend.

## The Product

DecisionOS aims to answer:

> **Which supplier should we choose, why, what could make that recommendation wrong, and what should we do next?**

The system will combine:

**Research → Evidence → Evaluation → Risk → Recommendation → Human decision**

Rather than producing a generic AI-generated answer, DecisionOS is designed around traceable evidence and explicit decision criteria.

## Initial Use Case

### Electronic Component Supplier Selection

A procurement professional needs to select a supplier for a strategically important purchase.

Example requirements:

* Minimum annual capacity
* Maximum acceptable lead time
* Required certifications
* Target price
* Technical specifications
* Geographic constraints
* Quality requirements

DecisionOS will evaluate candidate suppliers against these requirements and produce an evidence-backed recommendation.

## Core Features

### 1. Evidence-backed supplier comparison

Compare suppliers across configurable criteria and show the evidence behind each assessment.

### 2. Hard constraints

Separate non-negotiable requirements from weighted preferences.

### 3. Supplier scoring

Calculate transparent, deterministic scores based on the decision criteria.

### 4. Risk analysis

Identify financial, operational, geographic, compliance, and supply-chain risks.

### 5. Counter-evidence

Actively search for evidence that could challenge the initial recommendation.

### 6. Recommendation stability

Test how changes in assumptions, weights, price, lead time, or risk affect the final recommendation.

### 7. Recommended next action

Translate the analysis into a practical procurement action.

## Product Principle

> **AI recommends. Humans decide.**

DecisionOS is intended to support procurement professionals rather than autonomously award suppliers or make irreversible procurement decisions.

## Current Status

**Phase 1 — Product Discovery**

| Area                 | Status         |
| -------------------- | -------------- |
| Product hypothesis   | 🟢 Defined     |
| Initial user         | 🟢 Defined     |
| Initial use case     | 🟢 Defined     |
| Market research      | 🟡 In progress |
| Data strategy        | ⚪ Not started  |
| Architecture         | ⚪ Not started  |
| MVP                  | ⚪ Not started  |
| Evaluation framework | ⚪ Not started  |
| Deployment           | ⚪ Not started  |

## Planned Architecture

```text
                    BUSINESS REQUIREMENT
                             │
                             ▼
                       DECISION SETUP
                             │
                             ▼
                    RESEARCH & RETRIEVAL
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          Company          Market          Risk
           Data             Data           Data
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                       EVIDENCE LAYER
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
               Supporting       Contradicting
                Evidence          Evidence
                    │                 │
                    └────────┬────────┘
                             ▼
                     DECISION ENGINE
                             │
                             ▼
                     RECOMMENDATION
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
             Why this?          What could change it?
                  │                     │
                  └──────────┬──────────┘
                             ▼
                       HUMAN DECISION
```

## Evaluation

A major goal of this project is to evaluate the AI system rather than simply demonstrate that an LLM can generate an answer.

Planned evaluation areas include:

* Evidence retrieval accuracy
* Citation correctness
* Claim-to-source accuracy
* Contradiction detection
* Supplier scoring consistency
* Recommendation stability
* Hallucination rate
* Latency
* Cost per decision

## Project Roadmap

* [x] Product hypothesis
* [x] Initial user definition
* [x] Initial procurement use case
* [ ] Market and competitor validation
* [ ] Exact category validation
* [ ] Supplier data strategy
* [ ] Data model
* [ ] Product requirements
* [ ] System architecture
* [ ] Research engine
* [ ] Evidence layer
* [ ] Decision engine
* [ ] Counter-evidence engine
* [ ] Sensitivity analysis
* [ ] Web application
* [ ] Evaluation benchmark
* [ ] Deployment
* [ ] Product case study

## Why This Project?

The goal is to explore a broader question:

> **How can AI help people make better decisions when information is fragmented, uncertain, and contradictory?**

Procurement is the initial domain. The underlying decision-intelligence architecture could eventually be applied to other complex business decisions.

## Disclaimer

DecisionOS is an independent portfolio project and research prototype. It is not intended to provide professional procurement, financial, legal, compliance, or supply-chain advice.

## License

MIT
