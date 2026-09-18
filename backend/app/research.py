from typing import Literal

from pydantic import BaseModel, Field

from app.evidence import Evidence


class ResearchSource(BaseModel):
    source_name: str
    source_url: str
    content: str
    source_type: str


class ResearchRequest(BaseModel):
    question: str
    evidence: list[Evidence] = Field(default_factory=list)


class ResearchResponse(BaseModel):
    question: str
    status: str
    findings: list[Evidence]


class SourceRetrievalRequest(BaseModel):
    source_name: str
    source_url: str
    source_type: str
    content: str


def retrieve_source(
    request: SourceRetrievalRequest,
) -> ResearchSource:
    return ResearchSource(
        source_name=request.source_name,
        source_url=request.source_url,
        content=request.content,
        source_type=request.source_type,
    )

def research(request: ResearchRequest) -> ResearchResponse:
    return ResearchResponse(
        question=request.question,
        status="ready",
        findings=request.evidence,
    )

def create_evidence_from_source(
    source: ResearchSource,
    claim: str,
    evidence_type: Literal[
        "supporting",
        "contradicting",
        "neutral",
        "missing",
    ],
    confidence: float,
) -> Evidence:
    return Evidence(
        source_name=source.source_name,
        source_url=source.source_url,
        claim=claim,
        evidence_type=evidence_type,
        confidence=confidence,
    )