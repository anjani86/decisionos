from pydantic import BaseModel, Field


class CriterionScore(BaseModel):
    name: str
    weight: float = Field(ge=0.0, le=1.0)
    score: float = Field(ge=0.0, le=100.0)


class CriterionResult(BaseModel):
    name: str
    weight: float
    score: float
    weighted_contribution: float


class HardConstraints(BaseModel):
    max_lead_time_weeks: float | None = None
    max_price: float | None = None
    rohs_required: bool = False
    lifecycle_required: str | None = None


class DecisionRequest(BaseModel):
    option_name: str
    criteria: list[CriterionScore]

    lead_time_weeks: float | None = None
    price: float | None = None
    rohs_compliant: bool | None = None
    lifecycle_status: str | None = None

    hard_constraints: HardConstraints = HardConstraints()


class DecisionResponse(BaseModel):
    option_name: str
    eligibility: str
    overall_score: float
    recommendation: str
    criteria: list[CriterionResult]
    failed_constraints: list[str]

class SensitivityResult(BaseModel):
    parameter: str
    original_value: float
    changed_value: float
    original_score: float
    changed_score: float
    recommendation_changed: bool

def check_hard_constraints(request: DecisionRequest) -> list[str]:
    failed_constraints = []
    constraints = request.hard_constraints

    if (
        constraints.max_lead_time_weeks is not None
        and request.lead_time_weeks is not None
        and request.lead_time_weeks > constraints.max_lead_time_weeks
    ):
        failed_constraints.append(
            f"Lead time exceeds maximum of "
            f"{constraints.max_lead_time_weeks} weeks."
        )

    if (
        constraints.max_price is not None
        and request.price is not None
        and request.price > constraints.max_price
    ):
        failed_constraints.append(
            f"Price exceeds maximum of ${constraints.max_price}."
        )

    if constraints.rohs_required and request.rohs_compliant is not True:
        failed_constraints.append("RoHS compliance is required.")

    if (
        constraints.lifecycle_required is not None
        and request.lifecycle_status != constraints.lifecycle_required
    ):
        failed_constraints.append(
            f"Lifecycle status must be "
            f"'{constraints.lifecycle_required}'."
        )

    return failed_constraints


def calculate_criterion_results(
    request: DecisionRequest,
) -> list[CriterionResult]:
    return [
        CriterionResult(
            name=criterion.name,
            weight=criterion.weight,
            score=criterion.score,
            weighted_contribution=round(
                criterion.score * criterion.weight,
                2,
            ),
        )
        for criterion in request.criteria
    ]


def calculate_weighted_score(request: DecisionRequest) -> float:
    total_weight = sum(
        criterion.weight for criterion in request.criteria
    )

    if total_weight == 0:
        raise ValueError(
            "Total criterion weight must be greater than zero."
        )

    weighted_score = sum(
        criterion.score * criterion.weight
        for criterion in request.criteria
    )

    return weighted_score / total_weight


def calculate_decision(request: DecisionRequest) -> DecisionResponse:
    failed_constraints = check_hard_constraints(request)
    criterion_results = calculate_criterion_results(request)

    if failed_constraints:
        return DecisionResponse(
            option_name=request.option_name,
            eligibility="ineligible",
            overall_score=0.0,
            recommendation="not_recommended",
            criteria=criterion_results,
            failed_constraints=failed_constraints,
        )

    overall_score = calculate_weighted_score(request)

    if overall_score >= 80:
        recommendation = "recommended"
    elif overall_score >= 60:
        recommendation = "acceptable"
    else:
        recommendation = "not_recommended"

    return DecisionResponse(
        option_name=request.option_name,
        eligibility="eligible",
        overall_score=round(overall_score, 2),
        recommendation=recommendation,
        criteria=criterion_results,
        failed_constraints=[],
    )

def calculate_sensitivity(
    request: DecisionRequest,
    criterion_name: str,
    changed_score: float,
) -> SensitivityResult:
    original_score = calculate_weighted_score(request)

    modified_criteria = []

    for criterion in request.criteria:
        if criterion.name == criterion_name:
            modified_criteria.append(
                CriterionScore(
                    name=criterion.name,
                    weight=criterion.weight,
                    score=changed_score,
                )
            )
        else:
            modified_criteria.append(criterion)

    modified_request = DecisionRequest(
        option_name=request.option_name,
        criteria=modified_criteria,
        lead_time_weeks=request.lead_time_weeks,
        price=request.price,
        rohs_compliant=request.rohs_compliant,
        lifecycle_status=request.lifecycle_status,
        hard_constraints=request.hard_constraints,
    )

    new_score = calculate_weighted_score(modified_request)

    original_recommendation = (
        "recommended"
        if original_score >= 80
        else "acceptable"
        if original_score >= 60
        else "not_recommended"
    )

    changed_recommendation = (
        "recommended"
        if new_score >= 80
        else "acceptable"
        if new_score >= 60
        else "not_recommended"
    )

    original_value = next(
        criterion.score
        for criterion in request.criteria
        if criterion.name == criterion_name
    )

    return SensitivityResult(
        parameter=criterion_name,
        original_value=original_value,
        changed_value=changed_score,
        original_score=round(original_score, 2),
        changed_score=round(new_score, 2),
        recommendation_changed=(
            original_recommendation != changed_recommendation
        ),
    )
