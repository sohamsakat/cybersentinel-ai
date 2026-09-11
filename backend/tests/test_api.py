import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import Base, SessionLocal, engine
from app.main import seed_initial_data


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_initial_data(db)
    finally:
        db.close()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_auth_login(client):
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "analyst", "password": "analyst123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["role"] == "tier1_analyst"


def test_incidents_list_and_stats(client):
    auth_resp = client.post(
        "/api/v1/auth/login",
        data={"username": "analyst", "password": "analyst123"},
    )
    token = auth_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test Stats Endpoint
    stats_resp = client.get("/api/v1/incidents/stats/summary", headers=headers)
    assert stats_resp.status_code == 200
    stats = stats_resp.json()
    assert stats["total_incidents"] >= 2
    assert "critical_count" in stats

    # Test Incidents List
    inc_resp = client.get("/api/v1/incidents", headers=headers)
    assert inc_resp.status_code == 200
    incidents = inc_resp.json()
    assert len(incidents) >= 2


def test_secops_copilot_chat(client):
    auth_resp = client.post(
        "/api/v1/auth/login",
        data={"username": "analyst", "password": "analyst123"},
    )
    token = auth_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    chat_payload = {
        "message": "What is MITRE technique T1110 and how do we remediate it?",
        "incident_id": 1,
    }
    chat_resp = client.post("/api/v1/chat", json=chat_payload, headers=headers)
    assert chat_resp.status_code == 200
    chat_data = chat_resp.json()
    assert "answer" in chat_data
    assert len(chat_data["cited_sources"]) > 0


def test_incident_pdf_export(client):
    auth_resp = client.post(
        "/api/v1/auth/login",
        data={"username": "analyst", "password": "analyst123"},
    )
    token = auth_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    pdf_resp = client.get("/api/v1/reports/incident/1/pdf", headers=headers)
    assert pdf_resp.status_code == 200
    assert pdf_resp.headers["content-type"] == "application/pdf"
    assert pdf_resp.content.startswith(b"%PDF")
