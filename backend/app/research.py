from pydantic import BaseModel


class ResearchRequest(BaseModel):
    question: str


class ResearchResponse(BaseModel):
    question: str
    status: str
    message: str


def research(request: ResearchRequest) -> ResearchResponse:
    return ResearchResponse(
        question=request.question,
        status="not_implemented",
        message="Research engine not implemented yet.",
    )