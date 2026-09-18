from app.evidence import Evidence
from app.research import ResearchRequest, research


def test_research_returns_ready_response():
    request = ResearchRequest(
        question="Is STM32F407VGT6 an active product?"
    )

    result = research(request)

    assert result.question == request.question
    assert result.status == "ready"
    assert result.findings == []


def test_research_returns_supplied_evidence():
    evidence = Evidence(
        source_name="STMicroelectronics",
        source_url="https://www.st.com/",
        claim="STM32F407VGT6 is an active product",
        evidence_type="supporting",
        confidence=0.95,
    )

    request = ResearchRequest(
        question="Is STM32F407VGT6 an active product?",
        evidence=[evidence],
    )

    result = research(request)

    assert len(result.findings) == 1
    assert result.findings[0].source_name == "STMicroelectronics"
    assert result.findings[0].claim == (
        "STM32F407VGT6 is an active product"
    )
    assert result.findings[0].confidence == 0.95
