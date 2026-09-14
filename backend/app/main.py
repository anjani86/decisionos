from fastapi import FastAPI
from pydantic import BaseModel


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
