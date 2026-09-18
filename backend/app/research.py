from pydantic import BaseModel

from app.evidence import Evidence


class ResearchRequest(BaseModel):
    question: str
    evidence: list[Evidence] = []


class ResearchResponse(BaseModel):
    question: str
    status: str
    findings: list[Evidence]


def research(request: ResearchRequest) -> ResearchResponse:
    return ResearchResponse(
        question=request.question,
        status="ready",
        findings=request.evidence,
    )
