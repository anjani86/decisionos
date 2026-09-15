from pydantic import BaseModel, Field


class CriterionScore(BaseModel):
    name: str
    weight: float = Field(ge=0.0, le=1.0)
    score: float = Field(ge=0.0, le=100.0)


class DecisionRequest(BaseModel):
    option_name: str
    criteria: list[CriterionScore]


class DecisionResponse(BaseModel):
    option_name: str
    overall_score: float
    recommendation: str


def calculate_decision(request: DecisionRequest) -> DecisionResponse:
    total_weight = sum(criterion.weight for criterion in request.criteria)

    if total_weight == 0:
        raise ValueError("Total criterion weight must be greater than zero.")

    weighted_score = sum(
        criterion.score * criterion.weight
        for criterion in request.criteria
    )

    overall_score = weighted_score / total_weight

    if overall_score >= 80:
        recommendation = "recommended"
    elif overall_score >= 60:
        recommendation = "acceptable"
    else:
        recommendation = "not_recommended"

    return DecisionResponse(
        option_name=request.option_name,
        overall_score=round(overall_score, 2),
        recommendation=recommendation,
    )