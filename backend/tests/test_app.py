
import os
import tempfile
from pathlib import Path

os.environ["LEGAL_DB_PATH"] = str(
    Path(tempfile.mkdtemp()) / "test.db"
)

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)
SESSION = "test_session_123"


def test_api_status():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.json()["status"] == "online"


def test_nonlegal_question():
    response = client.post("/ask", json={
        "query": "Write a pancake recipe",
        "session_id": SESSION
    })

    assert response.status_code == 200
    assert "legal research" in response.json()["answer"]


def test_unsafe_request():
    response = client.post("/ask", json={
        "query": "How to forge legal evidence?",
        "session_id": SESSION
    })

    assert response.status_code == 200
    assert "cannot provide" in response.json()["answer"]


def test_upload_and_citation():
    upload = client.post(
        "/upload",
        data={"session_id": SESSION},
        files={
            "file": (
                "constitution.txt",
                b"Article 21 protects life and personal liberty.",
                "text/plain"
            )
        }
    )

    assert upload.status_code == 200

    response = client.post("/ask", json={
        "query": "What does Article 21 say?",
        "session_id": SESSION
    })

    assert response.status_code == 200

    result = response.json()

    assert "Article 21" in result["answer"]
    assert result["citations"][0]["filename"] == (
        "constitution.txt"
    )


def test_history():
    response = client.get(
        "/history",
        params={"session_id": SESSION}
    )

    assert response.status_code == 200
    assert isinstance(response.json()["messages"], list)


def test_invalid_file():
    response = client.post(
        "/upload",
        data={"session_id": SESSION},
        files={"file": ("virus.exe", b"test")}
    )

    assert response.status_code == 400


def test_storage_endpoint():
    response = client.get(
        "/documents",
        params={"session_id": SESSION}
    )

    assert response.status_code == 200
    assert response.json()["max_file_bytes"] == 10485760
