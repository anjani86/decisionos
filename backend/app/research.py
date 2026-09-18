from typing import Literal
from urllib.request import Request, urlopen

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


def retrieve_url(
    source_name: str,
    source_url: str,
    source_type: str,
    timeout: float = 10.0,
) -> ResearchSource:
    request = Request(
        source_url,
        headers={"User-Agent": "DecisionOS/0.1"},
    )

    with urlopen(request, timeout=timeout) as response:
        content = response.read().decode("utf-8")

    return ResearchSource(
        source_name=source_name,
        source_url=source_url,
        content=content,
        source_type=source_type,
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