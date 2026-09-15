from app.evidence import CriterionAssessment, Evidence
from app.decision import (
    CriterionScore,
    DecisionRequest,
    HardConstraints,
    calculate_decision,
)


def sample_criteria():
    return [
        CriterionScore(name="Technical Fit", weight=0.25, score=95),
        CriterionScore(name="Availability", weight=0.20, score=95),
        CriterionScore(name="Lead Time", weight=0.15, score=95),
        CriterionScore(name="Price", weight=0.15, score=95),
        CriterionScore(name="Lifecycle", weight=0.10, score=95),
        CriterionScore(name="Supply Risk", weight=0.10, score=95),
        CriterionScore(name="Geographic Risk", weight=0.05, score=95),
    ]


def sample_constraints():
    return HardConstraints(
        max_lead_time_weeks=12,
        max_price=2.5,
        rohs_required=True,
        lifecycle_required="active",
    )


def test_eligible_option_is_recommended():
    request = DecisionRequest(
        option_name="Supplier A",
        criteria=sample_criteria(),
        lead_time_weeks=8,
        price=2.0,
        rohs_compliant=True,
        lifecycle_status="active",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert result.eligibility == "eligible"
    assert result.overall_score == 95
    assert result.recommendation == "recommended"
    assert result.failed_constraints == []


def test_lead_time_violation_makes_option_ineligible():
    request = DecisionRequest(
        option_name="Supplier B",
        criteria=sample_criteria(),
        lead_time_weeks=18,
        price=2.0,
        rohs_compliant=True,
        lifecycle_status="active",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert result.eligibility == "ineligible"
    assert result.overall_score == 0
    assert result.recommendation == "not_recommended"
    assert "Lead time exceeds maximum of 12.0 weeks." in result.failed_constraints


def test_price_violation_makes_option_ineligible():
    request = DecisionRequest(
        option_name="Supplier C",
        criteria=sample_criteria(),
        lead_time_weeks=8,
        price=3.0,
        rohs_compliant=True,
        lifecycle_status="active",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert result.eligibility == "ineligible"
    assert "Price exceeds maximum of $2.5." in result.failed_constraints


def test_rohs_violation_makes_option_ineligible():
    request = DecisionRequest(
        option_name="Supplier D",
        criteria=sample_criteria(),
        lead_time_weeks=8,
        price=2.0,
        rohs_compliant=False,
        lifecycle_status="active",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert result.eligibility == "ineligible"
    assert "RoHS compliance is required." in result.failed_constraints


def test_lifecycle_violation_makes_option_ineligible():
    request = DecisionRequest(
        option_name="Supplier E",
        criteria=sample_criteria(),
        lead_time_weeks=8,
        price=2.0,
        rohs_compliant=True,
        lifecycle_status="obsolete",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert result.eligibility == "ineligible"
    assert (
        "Lifecycle status must be 'active'."
        in result.failed_constraints
    )


def test_multiple_constraint_failures_are_reported():
    request = DecisionRequest(
        option_name="Supplier F",
        criteria=sample_criteria(),
        lead_time_weeks=18,
        price=3.0,
        rohs_compliant=False,
        lifecycle_status="obsolete",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert result.eligibility == "ineligible"
    assert result.overall_score == 0
    assert len(result.failed_constraints) == 4

def test_decision_includes_criterion_explanations():
    request = DecisionRequest(
        option_name="Supplier G",
        criteria=sample_criteria(),
        lead_time_weeks=8,
        price=2.0,
        rohs_compliant=True,
        lifecycle_status="active",
        hard_constraints=sample_constraints(),
    )

    result = calculate_decision(request)

    assert len(result.criteria) == 7

    first = result.criteria[0]

    assert first.name == "Technical Fit"
    assert first.weight == 0.25
    assert first.score == 95
    assert first.weighted_contribution == 23.75

    total_contribution = sum(
        criterion.weighted_contribution
        for criterion in result.criteria
    )

    assert total_contribution == 95

def test_criterion_assessment_contains_evidence():
    evidence = Evidence(
        source_name="STMicroelectronics",
        source_url="https://www.st.com/",
        claim="STM32F407VGT6 is an active product",
        evidence_type="supporting",
        confidence=0.95,
    )

    assessment = CriterionAssessment(
        criterion_name="Lifecycle",
        assessment=(
            "The component is currently listed as an active "
            "product by the manufacturer."
        ),
        score=95,
        evidence=[evidence],
    )

    assert assessment.criterion_name == "Lifecycle"
    assert assessment.score == 95
    assert len(assessment.evidence) == 1
    assert assessment.evidence[0].source_name == "STMicroelectronics"
    assert assessment.evidence[0].confidence == 0.95    