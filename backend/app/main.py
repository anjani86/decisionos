from fastapi import FastAPI
from pydantic import BaseModel
from app.evidence import Evidence
from app.decision import DecisionRequest, DecisionResponse, calculate_decision

from app.research import ResearchRequest, ResearchResponse, research


app = FastAPI(
    title="DecisionOS API",
    description="Evidence-backed AI decision intelligence API",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


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