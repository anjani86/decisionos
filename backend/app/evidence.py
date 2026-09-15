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
    evidence: list[Evidence]
    counter_evidence: list[Evidence] = []