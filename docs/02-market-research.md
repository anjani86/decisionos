# Phase 2 — Market & Competitor Research

## 1. Market Context

Procurement is increasingly becoming a strategic decision-making function rather
than only a cost-management function.

AI adoption in procurement is growing, but enterprise adoption remains constrained
by data quality, fragmented systems, and limited proactive risk monitoring.

According to GEP's 2026 Procurement Executive Insight Report, approximately 17%
of organizations report moderate-to-large-scale deployment of agentic AI in
procurement, while 44% are actively piloting it.

The same research reports that only around 43% of purchasing categories have
proactive risk monitoring in place.

This creates an opportunity for AI systems that can help procurement teams move
from fragmented information toward faster and more defensible decisions.

## 2. Competitive Landscape

### McKinsey Spendscape

Spendscape provides AI-powered procurement intelligence across spend data,
supplier information, analytics, risk, and category strategy.

Key capabilities:
- Natural-language interaction with procurement data
- Supplier and category analysis
- Risk identification
- Spend analytics
- Scenario modelling
- Traceable insights

Implication for DecisionOS:

A generic procurement chatbot or procurement analytics dashboard would not be
sufficiently differentiated.

### GEP

GEP provides source-to-pay procurement software and AI-native supplier risk
management capabilities.

Key capabilities:
- Supplier risk assessment
- Continuous supplier monitoring
- Compliance monitoring
- Supplier management
- Procurement workflows
- AI agents

Implication for DecisionOS:

Supplier risk monitoring itself is already a mature product category.

### Exiger

Exiger provides AI-powered supply-chain and third-party risk intelligence.

Key capabilities:
- Supplier screening
- Risk monitoring
- Supply-chain intelligence
- Third-party risk management

Implication for DecisionOS:

Risk intelligence is valuable, but DecisionOS should focus on how evidence
changes a specific business decision rather than simply producing a risk score.

## 3. Initial Market Gap Hypothesis

The initial hypothesis is that DecisionOS should not attempt to replace
enterprise procurement platforms.

Instead, it should focus on a narrower decision workflow:

> Evidence → Evaluation → Risk → Counter-evidence → Sensitivity → Recommendation

The product should help a procurement professional understand not only:

"Which supplier scores highest?"

but also:

- Why does it score highest?
- What evidence supports the recommendation?
- What evidence contradicts it?
- Which assumptions matter most?
- What could change the recommendation?
- What should the procurement professional investigate next?

## 4. Product Differentiation Hypothesis

DecisionOS will explore:

### Evidence-backed recommendations

Every important supplier assessment should be connected to evidence.

### Counter-evidence

The system should actively search for information that challenges its
initial recommendation.

### Recommendation stability

The system should test whether the recommendation changes when important
assumptions or decision weights change.

### Human decision support

The system should recommend and explain rather than autonomously award a supplier.

> AI recommends. Humans decide.

## 5. Competitive Position

DecisionOS is NOT intended to compete with enterprise procurement suites.

It is a research and engineering prototype focused on one question:

> How can AI turn fragmented and sometimes contradictory supplier information
> into a transparent, challengeable, and defensible procurement decision?

The initial prototype will focus on supplier selection for strategically
important purchases.

## 6. Key Research Questions

Before implementation, we need to validate:

1. Which supplier-selection decisions are most difficult?
2. Which supplier attributes are hardest to verify?
3. Which evidence sources are considered trustworthy?
4. How frequently does supplier information contradict itself?
5. Which procurement categories have sufficient public data for an MVP?
6. Which category provides the strongest combination of:
   - data availability
   - decision complexity
   - AI opportunity
   - engineering challenge
   - product-management value
7. What existing products already solve the problem?
8. Where can a small research prototype demonstrate a meaningful difference?

## 7. Current Hypothesis

The current hypothesis is:

> DecisionOS can demonstrate a meaningful AI product capability by combining
> evidence retrieval, transparent decision criteria, supplier scoring,
> counter-evidence analysis, and sensitivity analysis into a single
> human-in-the-loop decision workflow.

This hypothesis must be validated before significant engineering investment.
