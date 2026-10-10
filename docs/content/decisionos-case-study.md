# DecisionOS: Evidence-Backed Supplier Decision Intelligence

## Project overview

DecisionOS is a portfolio project exploring how procurement teams can make more transparent, consistent, and evidence-backed supplier decisions.

It combines structured supplier evaluation, weighted scoring, eligibility rules, evidence records, and decision explanations through a Python API.

**Project type:** AI product and engineering prototype  
**Domain:** Procurement and supplier decision intelligence  
**Status:** MVP prototype  
**Repository:** https://github.com/anjani86/decisionos

## The problem

Supplier selection often involves balancing competing factors such as:

- Technical suitability
- Product availability
- Lead time
- Price
- Product lifecycle status
- Supply risk
- Geographic risk

A single overall score can make a decision appear simpler than it is. For example, a supplier with an attractive price might still violate a mandatory delivery deadline.

A useful decision-support system should distinguish between mandatory requirements and preferences, show how scores are calculated, and make supporting evidence and limitations visible.

This project explores a practical implementation of that approach.

## Product objective

Build an API that helps users compare supplier options and understand:

1. Which options satisfy mandatory constraints?
2. How do eligible options score against weighted criteria?
3. Why is an option recommended or rejected?
4. How sensitive is the result to changes in assumptions or weights?
5. What evidence supports or contradicts an assessment?

The intended outcome is decision support, not autonomous procurement approval.

## How the prototype works

The current workflow is:

1. Submit structured supplier options and evaluation criteria.
2. Check hard constraints such as maximum lead time and price.
3. Calculate weighted scores for eligible options.
4. Return a recommendation and criterion-level explanation.
5. Compare multiple options.
6. Explore sensitivity and stability under changed assumptions.
7. Associate evidence and counter-evidence with assessments.
8. Provide a URL-based source retrieval endpoint for research workflows.

The API is built with Python and FastAPI. Interactive API documentation is available through Swagger UI when the local server is running.

## Decision logic

The prototype uses configurable criterion weights and a deterministic weighted-scoring approach.

The current example criteria include:

| Criterion | Weight |
|---|---:|
| Technical fit | 25% |
| Availability | 20% |
| Lead time | 15% |
| Price | 15% |
| Lifecycle | 10% |
| Supply risk | 10% |
| Geographic risk | 5% |

These weights total 100%. They are prototype assumptions, not validated industry standards.

Hard constraints are evaluated separately from preference scoring. An option that violates a mandatory requirement can be marked ineligible rather than winning on its weighted score alone.

This distinction is important: a high score should not conceal a failure to meet a non-negotiable procurement requirement.

## Illustrative example

The repository's demo compares two supplier options for the same component.

- **Supplier A:** eligible, with an example overall score of 90.5 and a recommendation of `recommended`.
- **Supplier B:** ineligible because its lead time exceeds the configured maximum of 12 weeks.

These are illustrative demo inputs and outputs, not verified supplier quotations, independently validated product assessments, or evidence of real procurement savings.

The example demonstrates the decision logic rather than proving that the recommendations are correct for a real purchasing decision.

## Technical implementation

The prototype includes:

- A FastAPI application with a health endpoint.
- Structured request and response models.
- Weighted supplier scoring.
- Hard-constraint eligibility checks.
- Multi-option supplier comparison.
- Sensitivity and stability analysis.
- Evidence and counter-evidence structures.
- Confidence fields for criterion assessments.
- URL-based source retrieval.
- Automated tests for core behavior.

The project also includes product discovery, market research, data strategy, requirements, and architecture documentation.

## Validation and current limitations

The latest reported automated test run completed with **35 passed and 1 warning**.

The local demo also completed successfully when the API server was running.

These results validate the tested prototype behavior; they do not establish production readiness.

Important limitations include:

- The example weights and supplier data are illustrative.
- Evidence quality depends on the accuracy, relevance, and freshness of its sources.
- URL retrieval can fail or time out; successful retrieval does not itself establish that a claim is true.
- Deterministic scores reflect configured assumptions and inputs, not objective certainty.
- Real procurement use would require domain validation, stronger data-quality controls, security and operational reviews, and human oversight.

The source-retrieval path and its failure handling still require explicit validation before being described as production-ready.

## Product decisions and lessons

### Separate constraints from preferences

Mandatory requirements should be checked independently from weighted preferences. This avoids allowing a low price or strong technical score to compensate for a disqualifying constraint.

### Make recommendations explainable

A recommendation is more useful when users can inspect criterion scores, weights, failed constraints, and supporting or contradicting evidence.

### Treat evidence and confidence carefully

A confidence value is not proof that a claim is correct. Source credibility, recency, contradictory information, and missing evidence must remain visible to decision-makers.

### Make uncertainty part of the product

Sensitivity and stability analysis help users see whether a recommendation depends heavily on particular weights or assumptions.

## What I would improve next

After completing and validating the MVP, the next iterations could explore:

1. More robust and observable source retrieval with explicit error handling.
2. Evidence provenance, freshness, and claim-level traceability.
3. A representative, documented procurement dataset.
4. Evaluation cases that test whether recommendations behave sensibly under changed assumptions.
5. Feedback from procurement practitioners to validate workflows and criteria.
6. A user-facing decision review experience, if user research supports the need.

These are potential next steps, not features claimed to be complete.

## What this project demonstrates

DecisionOS is intended to demonstrate the intersection of product thinking and hands-on engineering:

- Turning a domain problem into explicit requirements.
- Translating product rules into API contracts and testable behavior.
- Making trade-offs and constraints visible.
- Designing explainability and evidence into a decision workflow.
- Documenting assumptions, limitations, and future validation needs.

The project is an evolving prototype. Its value lies in the problem framing, implementation, and validation process—not in claiming unproven business outcomes.

## Demo and repository

Repository: https://github.com/anjani86/decisionos

To run the project locally, follow the setup and demo instructions in the repository README. The API's Swagger documentation is available at `/docs` while the local server is running.
