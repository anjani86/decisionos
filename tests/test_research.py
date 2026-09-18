from app.research import ResearchRequest, research


def test_research_returns_ready_response():
    request = ResearchRequest(
        question="Is STM32F407VGT6 an active product?"
    )

    result = research(request)

    assert result.question == request.question
    assert result.status == "ready"
    assert result.findings == []


def test_research_starts_with_no_findings():
    request = ResearchRequest(
        question="Which supplier has the lowest lead time?"
    )

    result = research(request)

    assert result.findings == []
