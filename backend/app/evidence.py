from typing import Literal

from pydantic import BaseModel, Field


class Evidence(BaseModel):
    source_name: str
    source_url: str
    claim: str
    evidence_type: Literal[
        "supporting",
        "contradicting",
        "neutral",
        "missing",
    ]
    confidence: float = Field(ge=0.0, le=1.0)


class CriterionAssessment(BaseModel):
    criterion_name: str
    assessment: str
    score: float = Field(ge=0.0, le=100.0)
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    evidence: list[Evidence]
    counter_evidence: list[Evidence] = Field(
        default_factory=list
    )


def calculate_assessment_confidence(
    evidence: list[Evidence],
) -> float:
    if not evidence:
        return 0.0

    return round(
        sum(item.confidence for item in evidence)
        / len(evidence),
        2,
    )


def create_criterion_assessment(
    criterion_name: str,
    assessment: str,
    score: float,
    evidence: list[Evidence],
    counter_evidence: list[Evidence] | None = None,
) -> CriterionAssessment:
    counter_evidence = counter_evidence or []

    confidence = calculate_assessment_confidence(evidence)

    return CriterionAssessment(
        criterion_name=criterion_name,
        assessment=assessment,
        score=score,
        confidence=confidence,
        evidence=evidence,
        counter_evidence=counter_evidence,
    )