# Phase 3 — Data Strategy

## 1. Objective

DecisionOS requires reliable evidence to evaluate electronic component sourcing
and supplier/option-selection decisions.

The data strategy is designed around one principle:

> Every important decision claim should be traceable to evidence.

The system should distinguish between:

* Source data
* Extracted evidence
* AI-generated interpretation
* Deterministic calculations
* Final recommendation

AI should interpret evidence, but should not invent supplier facts or perform
opaque scoring.

---

## 2. Initial Decision Scenario

The initial prototype will focus on:

> Which sourcing option should a company choose for a critical electronic
> component?

Example decision:

A company needs 100,000 units of an industrial electronic component annually.

DecisionOS evaluates candidate sourcing options based on:

* Technical compatibility
* Availability
* Lead time
* Price
* Lifecycle status
* Quality/certification evidence
* Authorized-source status
* Supply-chain risk
* Geographic risk
* Supplier reliability

---

## 3. Data Categories

DecisionOS will initially work with six major data categories.

### 3.1 Component/Product Data

Examples:

* Manufacturer
* Part number
* Product category
* Technical specifications
* Operating characteristics
* Package
* Datasheet
* Lifecycle status
* Compliance information
* Suggested replacements

Potential sources include:

* Manufacturer product pages
* Authorized distributors
* Distributor APIs
* Product datasheets

---

### 3.2 Commercial Data

Examples:

* Unit price
* Price breaks
* Minimum order quantity
* Availability
* Stock quantity
* Lead time
* Order constraints

Potential sources include:

* Distributor APIs
* Supplier catalogs
* Supplier/product pages
* Controlled prototype data

Commercial information can change frequently and should therefore include
a retrieval timestamp.

---

### 3.3 Supplier Data

Examples:

* Supplier identity
* Manufacturer/distributor relationship
* Certifications
* Quality programs
* Geographic presence
* Manufacturing/distribution locations
* Authorized-source status

Potential sources include:

* Supplier websites
* Certification documents
* Manufacturer authorization information
* Public company information

---

### 3.4 Supply-Chain Risk Data

Examples:

* Component shortages
* Lead-time changes
* Allocation
* Obsolescence
* Geographic concentration
* Geopolitical exposure
* Logistics disruption
* Industry-specific supply constraints

Potential sources include:

* Public industry reports
* Government publications
* Supplier/manufacturer announcements
* Reputable news sources
* Public supply-chain datasets

Risk evidence must include the source and publication/retrieval date.

---

### 3.5 Company and Financial Information

Where relevant, DecisionOS may use:

* Company size
* Revenue indicators
* Financial stability signals
* Corporate ownership
* Public filings
* Major business changes

Potential sources include:

* Public company filings
* Company websites
* Public financial databases
* Government/company registries where available

Financial data should not be presented as definitive financial advice.

---

### 3.6 Internal Decision Requirements

Some of the most important data will come directly from the user.

Examples:

* Required annual quantity
* Maximum acceptable lead time
* Maximum price
* Required certifications
* Technical requirements
* Geographic restrictions
* Risk tolerance
* Decision weights

This data is not retrieved from the web.

It represents the company's decision context.

---

## 4. Evidence Model

DecisionOS should represent evidence explicitly.

The conceptual chain is:

Source
→ Evidence
→ Claim
→ Criterion
→ Supplier/Option Assessment
→ Score
→ Recommendation

Example:

Source:

Manufacturer product page

↓

Evidence:

Part is listed as active production.

↓

Claim:

The component has an active lifecycle status.

↓

Criterion:

Lifecycle status

↓

Assessment:

Pass

↓

Decision impact:

Positive

This structure allows the user to inspect why a recommendation was produced.

---

## 5. Source Metadata

Every external evidence item should store metadata such as:

* Source URL
* Source title
* Publisher
* Publication date when available
* Retrieval timestamp
* Source type
* Evidence text
* Related supplier/component
* Related criterion
* Confidence
* Evidence status

Example:

```text
Source:
Manufacturer product page

Evidence:
Product listed as active.

Retrieved:
2026-09-14

Criterion:
Lifecycle

Assessment:
Positive

Confidence:
High
```

---

## 6. Evidence Types

DecisionOS should distinguish at least four evidence states:

### Supporting Evidence

Evidence that supports the current assessment.

### Contradicting Evidence

Evidence that conflicts with the current assessment.

### Neutral Evidence

Information that is relevant but does not materially change the assessment.

### Missing Evidence

Information required for a decision but not currently available.

Missing evidence is important.

The system should not convert lack of evidence into a positive or negative claim.

---

## 7. Source Reliability

Not all sources should be treated equally.

The initial source hierarchy is:

### Tier 1 — Primary Sources

Examples:

* Manufacturer documentation
* Supplier documentation
* Government publications
* Regulatory filings
* Official certification documents

Highest expected reliability.

### Tier 2 — Authorized/Structured Sources

Examples:

* Authorized distributor data
* Established industry databases
* Recognized technical databases

Generally high reliability, but information should still be validated.

### Tier 3 — Secondary Sources

Examples:

* Industry publications
* Reputable news organizations
* Analyst reports

Useful particularly for market and risk signals.

### Tier 4 — Unverified Sources

Examples:

* Forums
* Anonymous posts
* User-generated claims

These should not be treated as strong evidence without corroboration.

---

## 8. Real Data vs Controlled Prototype Data

The first MVP will not attempt to obtain every possible procurement dataset.

Instead, the project will deliberately separate:

### Real Data

Used where public or API-accessible information is available.

Examples:

* Component specifications
* Datasheets
* Product availability
* Lifecycle information
* Distributor information
* Public supplier documentation

### Controlled Prototype Data

Used where reliable public data is difficult to obtain.

Examples:

* Internal procurement requirements
* Example supplier quotes
* Decision weights
* Simulated annual demand
* Example supplier-specific operational assumptions

Controlled prototype data will be clearly labeled as simulated.

The goal is to demonstrate the decision architecture without pretending that
simulated information is real-world supplier intelligence.

---

## 9. Initial Data Sources

The prototype will investigate the following sources:

### DigiKey

Potential uses:

* Component catalog information
* Availability
* Pricing
* Technical specifications
* Product documentation

### Mouser

Potential uses:

* Component information
* Availability
* Pricing
* Lifecycle information
* Technical documentation
* Lead-time information

### Manufacturer Websites

Potential uses:

* Datasheets
* Product lifecycle
* Technical specifications
* Certifications
* Product announcements

### Public Industry Sources

Potential uses:

* Supply-chain disruption
* Component shortages
* Market conditions
* Geopolitical risk
* Industry trends

These sources will be evaluated before being included in the production
research pipeline.

---

## 10. API Strategy

Where an official API exists, DecisionOS should prefer the API over
unstructured scraping.

Benefits include:

* More consistent data
* Better reproducibility
* Lower parsing complexity
* Clearer usage policies
* Easier testing
* More reliable structured fields

API credentials must never be committed to GitHub.

Secrets will be stored using environment variables.

Example:

```text
MOUSER_API_KEY=
DIGIKEY_CLIENT_ID=
DIGIKEY_CLIENT_SECRET=
LLM_API_KEY=
```

Actual credentials must never be placed in source code, documentation, or
committed files.

---

## 11. Web Research Strategy

Not all evidence will be available through APIs.

For web-based research, the system should:

1. Search for relevant sources.
2. Retrieve the source.
3. Extract relevant evidence.
4. Store the source metadata.
5. Associate evidence with a specific claim.
6. Detect supporting and contradicting evidence.
7. Present citations to the user.

The system should never treat a search-result snippet as sufficient evidence
for an important procurement decision.

Whenever possible, the underlying source should be retrieved and inspected.

---

## 12. Evidence Freshness

Different evidence types have different useful lifetimes.

For example:

| Evidence                 | Expected freshness |
| ------------------------ | ------------------ |
| Component specifications | Long-lived         |
| Datasheet                | Long-lived         |
| Certification            | Medium             |
| Lifecycle status         | Medium             |
| Price                    | Short              |
| Availability             | Very short         |
| Lead time                | Very short         |
| Supply-chain risk        | Short              |
| News                     | Very short         |

DecisionOS should store retrieval timestamps so that users can understand
when the evidence was collected.

---

## 13. Data Model — Initial Concept

The initial database model will likely contain entities such as:

```text
Component
Supplier
SourcingOption
Criterion
Decision
Source
Evidence
Assessment
RiskSignal
Recommendation
```

Relationships:

```text
Component
   ↓
SourcingOption
   ↓
Supplier

Source
   ↓
Evidence
   ↓
Assessment
   ↓
Criterion
   ↓
Decision
   ↓
Recommendation
```

---

## 14. Data Quality Risks

The project must explicitly account for:

### Stale information

Prices, stock and lead times can change rapidly.

### Conflicting information

Different sources may report different values.

### Missing information

A supplier may not publicly disclose an important attribute.

### Ambiguous claims

A source may describe a product without explicitly confirming the required
criterion.

### Duplicate entities

The same supplier or component may appear under different identifiers.

### AI extraction errors

LLMs may incorrectly interpret technical or commercial information.

These risks will become part of the evaluation framework.

---

## 15. Contradiction Handling

When sources disagree, DecisionOS should not silently choose one.

Example:

```text
Source A:
Lead time = 8 weeks

Source B:
Lead time = 20 weeks
```

The system should surface the disagreement.

Possible output:

> Lead-time evidence is conflicting. Source A reports 8 weeks while Source B
> reports 20 weeks. The recommendation has therefore been marked as lower
> confidence.

This is preferable to hiding uncertainty behind a single AI-generated answer.

---

## 16. Initial Evaluation Dataset

The MVP should contain a small controlled benchmark.

Initial target:

* 5–10 components
* 3–5 sourcing options per component
* Multiple decision scenarios
* Supporting evidence
* Contradicting evidence
* Missing evidence
* Different decision weights

Each scenario should have an expected outcome or evaluation criteria.

The benchmark will later be used to test:

* Evidence retrieval
* Citation accuracy
* Claim extraction
* Contradiction detection
* Scoring consistency
* Recommendation stability

---

## 17. Data Governance Principles

DecisionOS should follow these principles:

1. Cite important claims.
2. Store source metadata.
3. Separate evidence from inference.
4. Separate deterministic calculations from LLM reasoning.
5. Never treat missing evidence as positive evidence.
6. Surface contradictions.
7. Timestamp volatile information.
8. Clearly label simulated data.
9. Never commit API credentials.
10. Keep humans responsible for the final procurement decision.

---

## 18. Initial Data Strategy Decision

For the MVP, DecisionOS will use:

> **Real public/API-accessible component and supplier information + controlled
> prototype procurement scenarios + cited public risk evidence.**

The system will prioritize evidence quality and traceability over dataset size.

The goal is not to build the largest procurement database.

The goal is to demonstrate that AI can transform fragmented evidence into a
transparent and challengeable business decision.

---

## 19. Next Phase

After the data strategy is validated, the next step is:

> **Define the product requirements and decision workflow.**

This will specify exactly what a user does from:

```text
Create Decision
        ↓
Define Requirements
        ↓
Add Candidate Options
        ↓
Research
        ↓
Review Evidence
        ↓
Evaluate
        ↓
Challenge Recommendation
        ↓
Sensitivity Analysis
        ↓
Final Recommendation
```

Only after this workflow is defined should implementation begin.

