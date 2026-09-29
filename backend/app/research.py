
from typing import Literal
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from fastapi import HTTPException
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


class URLRetrievalRequest(BaseModel):
    source_name: str
    source_url: str
    source_type: str


def retrieve_url(
    source_name: str,
    source_url: str,
    source_type: str,
    timeout: float = 15.0,
) -> ResearchSource:
    current_url = source_url

    for _ in range(5):
        request = Request(
            current_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/153.0.0.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml",
            },
        )

        try:
            with urlopen(request, timeout=timeout) as response:
                headers = getattr(response, "headers", None)

                if headers is not None:
                    charset = headers.get_content_charset() or "utf-8"
                else:
                    charset = "utf-8"

                content = response.read().decode(
                    charset,
                    errors="replace",
                )

                return ResearchSource(
                    source_name=source_name,
                    source_url=current_url,
                    content=content,
                    source_type=source_type,
                )

        except HTTPError as exc:
            if exc.code in {301, 302, 303, 307, 308}:
                location = exc.headers.get("Location")

                if not location:
                    raise HTTPException(
                        status_code=502,
                        detail="Source returned a redirect without a location.",
                    ) from exc

                current_url = urljoin(current_url, location)
                continue

            raise HTTPException(
                status_code=502,
                detail=f"Source returned HTTP {exc.code}: {current_url}",
            ) from exc

        except (URLError, TimeoutError) as exc:
            raise HTTPException(
                status_code=504,
                detail=f"Source retrieval timed out or failed: {current_url}",
            ) from exc

    raise HTTPException(
        status_code=502,
        detail="Source exceeded the maximum redirect limit.",
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