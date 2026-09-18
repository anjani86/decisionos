from app.evidence import Evidence

from app.research import (
    ResearchRequest,
    ResearchSource,
    SourceRetrievalRequest,
    create_evidence_from_source,
    research,
    retrieve_source,
)


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

def test_research_source_captures_source_material():
    source = ResearchSource(
        source_name="STMicroelectronics",
        source_url="https://www.st.com/",
        content="STM32F407VGT6 is an active product.",
        source_type="official_product_page",
    )

    assert source.source_name == "STMicroelectronics"
    assert source.source_url == "https://www.st.com/"
    assert source.content == "STM32F407VGT6 is an active product."
    assert source.source_type == "official_product_page"
def test_research_source_can_be_normalized_into_evidence():
    source = ResearchSource(
        source_name="STMicroelectronics",
        source_url="https://www.st.com/",
        content="STM32F407VGT6 is an active product.",
        source_type="official_product_page",
    )

    evidence = create_evidence_from_source(
        source=source,
        claim="STM32F407VGT6 is an active product",
        evidence_type="supporting",
        confidence=0.95,
    )

    assert evidence.source_name == "STMicroelectronics"
    assert evidence.source_url == "https://www.st.com/"
    assert evidence.claim == "STM32F407VGT6 is an active product"
    assert evidence.evidence_type == "supporting"
    assert evidence.confidence == 0.95


def test_retrieve_source_returns_research_source():
    request = SourceRetrievalRequest(
        source_name="STMicroelectronics",
        source_url="https://www.st.com/",
        source_type="official_product_page",
        content="STM32F407VGT6 is an active product.",
    )

    source = retrieve_source(request)

    assert source.source_name == "STMicroelectronics"
    assert source.source_url == "https://www.st.com/"
    assert source.source_type == "official_product_page"
    assert source.content == "STM32F407VGT6 is an active product."