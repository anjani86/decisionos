from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_source_evidence_endpoint_creates_evidence():
    response = client.post(
        "/source/evidence",
        json={
            "source": {
                "source_name": "STMicroelectronics",
                "source_url": "https://www.st.com/",
                "content": "STM32F407VGT6 is an active product.",
                "source_type": "official_product_page",
            },
            "claim": "STM32F407VGT6 is an active product",
            "evidence_type": "supporting",
            "confidence": 0.95,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["source_name"] == "STMicroelectronics"
    assert data["source_url"] == "https://www.st.com/"
    assert data["claim"] == "STM32F407VGT6 is an active product"
    assert data["evidence_type"] == "supporting"
    assert data["confidence"] == 0.95


def test_source_evidence_endpoint_rejects_invalid_evidence_type():
    response = client.post(
        "/source/evidence",
        json={
            "source": {
                "source_name": "STMicroelectronics",
                "source_url": "https://www.st.com/",
                "content": "STM32F407VGT6 is an active product.",
                "source_type": "official_product_page",
            },
            "claim": "STM32F407VGT6 is an active product",
            "evidence_type": "unsupported",
            "confidence": 0.95,
        },
    )

    assert response.status_code == 422
