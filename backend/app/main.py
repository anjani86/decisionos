from fastapi import FastAPI
from typing import Literal
from pydantic import BaseModel
from app.evidence import CriterionAssessment, Evidence, create_criterion_assessment
from app.decision import (
    ComparisonRequest,
    ComparisonResult,
    DecisionRequest,
    DecisionResponse,
    SensitivityResult,
    StabilityResult,
    calculate_comparison,
    calculate_decision,
    calculate_sensitivity,
    calculate_stability,
)

from app.research import (
    ResearchRequest,
    ResearchResponse,
    ResearchSource,
    SourceRetrievalRequest,
    create_evidence_from_source,
    research,
    retrieve_source,
)


app = FastAPI(
    title="DecisionOS API",
    description="Evidence-backed AI decision intelligence API",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

class SourceEvidenceRequest(BaseModel):
    source: ResearchSource
    claim: str
    evidence_type: Literal[
        "supporting",
        "contradicting",
        "neutral",
        "missing",
    ]
    confidence: float

@app.post("/source/retrieve", response_model=ResearchSource)
def source_retrieve_endpoint(request: SourceRetrievalRequest):
    return retrieve_source(request)


@app.post("/source/evidence", response_model=Evidence)
def source_evidence_endpoint(request: SourceEvidenceRequest):
    return create_evidence_from_source(
        source=request.source,
        claim=request.claim,
        evidence_type=request.evidence_type,
        confidence=request.confidence,
    )

@app.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="ok",
        service="decisionos-api",
        version="0.1.0",
    )


@app.post("/research", response_model=ResearchResponse)
def research_endpoint(request: ResearchRequest):
    return research(request)

@app.post("/evidence", response_model=Evidence)
def create_evidence(evidence: Evidence):
    return evidence

@app.post("/decision", response_model=DecisionResponse)
def decision_endpoint(request: DecisionRequest):
    return calculate_decision(request)

class AssessmentRequest(BaseModel):
    criterion_name: str
    assessment: str
    score: float
    evidence: list[Evidence]
    counter_evidence: list[Evidence] = []


@app.post("/assessment", response_model=CriterionAssessment)
def create_assessment(request: AssessmentRequest):
    return create_criterion_assessment(
        criterion_name=request.criterion_name,
        assessment=request.assessment,
        score=request.score,
        evidence=request.evidence,
        counter_evidence=request.counter_evidence,
    )

@app.post("/sensitivity", response_model=SensitivityResult)
def sensitivity_endpoint(
    request: DecisionRequest,
    criterion_name: str,
    changed_score: float,
):
    return calculate_sensitivity(
        request,
        criterion_name,
        changed_score,
    )

@app.post("/stability", response_model=StabilityResult)
def stability_endpoint(
    request: DecisionRequest,
    criterion_name: str,
    minimum_score: float = 0,
    step: float = 5,
):
    return calculate_stability(
        request,
        criterion_name,
        minimum_score,
        step,
    )

@app.post("/comparison", response_model=ComparisonResult)
def comparison_endpoint(
    request: ComparisonRequest,
):
    return calculate_comparison(request)