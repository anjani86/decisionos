# Phase 4 — Product Requirements

## 1. Product Objective

DecisionOS is an evidence-backed AI decision-support system for evaluating critical electronic component sourcing options.

The MVP helps procurement professionals move from fragmented supplier and component information to a transparent, evidence-backed, and challengeable sourcing recommendation.

DecisionOS is decision support, not autonomous procurement.

> **AI recommends. Humans decide.**

---

## 2. Primary User

### Strategic Procurement Manager

The primary user is responsible for evaluating sourcing options for an important component or procurement decision.

The user may need to balance:

* Technical requirements
* Cost
* Availability
* Lead time
* Lifecycle
* Supplier reliability
* Supply-chain risk
* Geographic risk
* Compliance requirements

---

## 3. Core User Story

> As a Strategic Procurement Manager, I want to compare sourcing options for a critical electronic component using evidence-backed AI analysis so that I can make a faster and more defensible sourcing decision.

---

## 4. Initial Decision

The MVP answers:

> **Which sourcing option should we choose for a critical electronic component?**

The system explains:

1. Which option is recommended?
2. Why is it recommended?
3. What evidence supports the recommendation?
4. What evidence contradicts it?
5. What could make the recommendation wrong?
6. How sensitive is the recommendation to changes in assumptions?
7. What should the procurement professional do next?

---

## 5. User Workflow

```text
Create Decision
      ↓
Define Requirements
      ↓
Define Hard Constraints
      ↓
Define Weighted Criteria
      ↓
Add Candidate Options
      ↓
Research Evidence
      ↓
Evaluate Options
      ↓
Review Evidence
      ↓
Generate Recommendation
      ↓
Challenge Recommendation
      ↓
Sensitivity Analysis
      ↓
Human Decision
```

---

# 6. Functional Requirements

## FR-01 — Create Decision

The user can create a procurement decision.

Required information:

* Decision name
* Component/product
* Annual demand
* Decision description
* Target decision date

Example:

```text
Decision:
Industrial MCU sourcing

Annual demand:
100,000 units

Decision date:
2026-10-01
```

---

## FR-02 — Define Technical Requirements

The user can specify technical requirements.

Examples:

* Voltage
* Package
* Operating temperature
* Performance
* Interface
* Memory
* Form factor
* Manufacturer restrictions

Requirements are classified as:

* Required
* Preferred

Required requirements are treated as hard constraints.

Preferred requirements contribute to the weighted score.

---

## FR-03 — Define Commercial Requirements

The user can define:

* Maximum unit price
* Target price
* Minimum order quantity
* Annual quantity
* Maximum acceptable lead time

Commercial requirements may be hard constraints or weighted criteria.

---

## FR-04 — Define Compliance Requirements

The user can specify required compliance or certification.

Examples:

* RoHS
* REACH
* ISO-related supplier requirements
* Industry-specific certifications

Required compliance conditions are treated as hard constraints where appropriate.

---

## FR-05 — Define Hard Constraints

Hard constraints represent non-negotiable requirements.

Example:

```text
Lead time <= 12 weeks
Annual capacity >= 100,000
RoHS = Required
Operating temperature >= required threshold
```

A sourcing option that fails a hard constraint is marked:

> **Ineligible**

It does not simply receive a lower weighted score.

---

## FR-06 — Define Weighted Criteria

The user can define decision criteria and weights.

Initial example:

| Criterion       | Weight |
| --------------- | -----: |
| Technical fit   |    25% |
| Availability    |    20% |
| Lead time       |    15% |
| Price           |    15% |
| Lifecycle       |    10% |
| Supply risk     |    10% |
| Geographic risk |     5% |

Weights must total 100%.

Weights are configurable and stored with each decision so that the recommendation can be reproduced.

---

## FR-07 — Add Candidate Options

The user can add candidate sourcing options.

A sourcing option may contain:

* Manufacturer
* Part number
* Distributor/supplier
* Unit price
* Availability
* Lead time
* Lifecycle
* Technical specifications
* Compliance information

Candidate options may initially be entered manually.

Later versions may discover candidate options through APIs or research.

---

## FR-08 — Research Evidence

DecisionOS retrieves evidence relevant to the decision.

Research focuses on:

* Technical fit
* Availability
* Price
* Lead time
* Lifecycle
* Compliance
* Supplier information
* Supply-chain risk
* Geographic risk

Every important external claim includes source information.

---

## FR-09 — Evidence Review

The user can inspect evidence supporting an assessment.

Each evidence item displays:

* Source
* Source title
* URL
* Retrieval date
* Evidence text
* Related criterion
* Assessment
* Confidence

Evidence is classified as:

* Supporting evidence
* Contradicting evidence
* Missing evidence

---

## FR-10 — Evidence-Based Assessment

DecisionOS converts evidence into structured assessments.

Example:

```text
Criterion:
Lead time

Evidence:
Distributor reports 8-week lead time.

Assessment:
Pass

Confidence:
High

Source:
Distributor product listing
```

The LLM may assist with interpretation.

Final numerical scoring is performed deterministically.

---

## FR-11 — Sourcing Option Scoring

DecisionOS calculates a transparent score.

Example:

```text
Technical fit       92
Availability        85
Lead time           90
Price               75
Lifecycle           95
Supply risk         70
Geographic risk     90
```

The weighted score is calculated by deterministic application logic.

The LLM does not perform the final arithmetic.

---

## FR-12 — Recommendation

DecisionOS generates a recommendation after evaluating eligible options.

Example:

> **Recommended option: Supplier A**

The recommendation includes:

* Overall score
* Hard-constraint status
* Major strengths
* Major weaknesses
* Supporting evidence
* Contradicting evidence
* Confidence
* Key decision drivers

---

## FR-13 — Recommendation Explanation

The system answers:

> **Why this option?**

The explanation references the most important decision drivers.

Example:

> Supplier A is recommended because it satisfies all mandatory requirements and has stronger evidence for availability and lead time. Supplier B has a lower price but significantly higher lead-time risk.

The explanation is traceable to the underlying assessments.

---

## FR-14 — Counter-Evidence

The user can challenge the recommendation.

Primary interaction:

> **What could make this recommendation wrong?**

DecisionOS searches for evidence that could weaken the recommendation.

Example:

```text
Potential challenge:

Supplier A's lead-time advantage may not hold if the current allocation
situation persists.

Evidence:
[Source]

Impact:
Medium

Recommendation impact:
Potentially significant
```

---

## FR-15 — Sensitivity Analysis

The user can change important assumptions.

Examples:

* Increase price weighting
* Increase supply-risk weighting
* Change maximum lead time
* Change annual demand
* Change risk tolerance

The system recalculates the recommendation.

Example:

```text
Current weights:
Supplier A → Recommended

Price weight increased:
Supplier B → Recommended
```

The system clearly shows:

> **What changed the decision?**

---

## FR-16 — Recommendation Stability

DecisionOS indicates whether the recommendation is stable.

### High Stability

The same option remains first across reasonable weight changes.

### Medium Stability

The recommendation changes under some plausible scenarios.

### Low Stability

Small changes in assumptions produce different recommendations.

This helps the user understand whether the decision is robust or fragile.

---

## FR-17 — Missing Evidence

When important information is unavailable, the system explicitly shows:

> **Evidence unavailable**

It does not infer a positive or negative assessment simply because evidence is missing.

Example:

```text
Supplier capacity:
No reliable public evidence found.

Assessment:
Unknown

Decision impact:
Requires human verification
```

---

## FR-18 — Contradictory Evidence

When sources disagree, DecisionOS surfaces the disagreement.

Example:

```text
Source A:
Lead time = 8 weeks

Source B:
Lead time = 20 weeks

Status:
Conflicting evidence

Confidence:
Low
```

The system does not silently select one source.

---

## FR-19 — Human Decision

The final decision remains with the user.

The user can record:

* Selected option
* Decision status
* Decision rationale
* Additional notes

Example:

```text
Decision:
Supplier A selected

Human rationale:
Selected because production continuity was prioritized over lowest unit cost.
```

The human decision may differ from the AI recommendation.

This is an intentional product capability.

---

# 7. Non-Functional Requirements

## NFR-01 — Traceability

Important recommendations are traceable through:

```text
Source
→ Evidence
→ Claim
→ Criterion
→ Assessment
→ Score
→ Recommendation
```

---

## NFR-02 — Reproducibility

Given the same:

* Decision requirements
* Candidate options
* Evidence
* Criteria
* Weights

the deterministic scoring system produces the same result.

---

## NFR-03 — Explainability

Users can understand why an option was recommended.

The product prioritizes specific, evidence-linked explanations over generic AI-generated reasoning.

---

## NFR-04 — Human Oversight

The system provides clear opportunities for:

* Review
* Challenge
* Override
* Final human decision

The AI does not autonomously award a supplier.

---

## NFR-05 — Uncertainty

The system represents uncertainty using:

* High
* Medium
* Low
* Unknown

Confidence reflects evidence quality rather than simply LLM confidence.

---

## NFR-06 — Freshness

Volatile information such as:

* Price
* Availability
* Lead time
* Supply risk

includes retrieval timestamps.

---

## NFR-07 — Security

API keys and credentials are never stored in the repository.

Secrets are provided through environment variables.

---

# 8. MVP Scope

The first working MVP includes:

### Decision Setup

* Create decision
* Define requirements
* Define constraints
* Define weights

### Candidate Evaluation

* Add candidate options
* Research evidence
* Evaluate criteria
* Calculate scores

### Decision Intelligence

* Recommendation
* Evidence explanation
* Counter-evidence
* Sensitivity analysis
* Recommendation stability

### Human Control

* Review
* Override
* Record final decision

---

# 9. Explicitly Out of Scope

The MVP does not include:

* Automatic purchase orders
* Autonomous supplier contracting
* ERP integration
* Supplier negotiation
* Payment processing
* Enterprise procurement workflow
* Large-scale supplier marketplace
* Full BOM management
* Real-time global supply-chain monitoring
* Autonomous procurement agents

---

# 10. Success Criteria

The MVP is successful if a user can:

1. Create a sourcing decision.
2. Define requirements.
3. Add multiple candidate options.
4. Retrieve relevant evidence.
5. See supporting and contradicting evidence.
6. Apply transparent scoring.
7. Receive an evidence-backed recommendation.
8. Challenge the recommendation.
9. Run sensitivity analysis.
10. Understand when the recommendation is unstable.
11. Override the AI recommendation.
12. Record the final human decision.

---

# 11. Product Principle

The central product principle is:

> **AI recommends. Humans decide.**

The purpose of DecisionOS is not to remove human procurement judgment.

The purpose is to make that judgment:

* Faster
* Better informed
* More transparent
* More evidence-backed
* Easier to challenge
* Easier to defend

