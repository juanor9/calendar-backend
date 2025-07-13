from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_query():
    query = {
        "query": """
        query {
            hello
        }
        """
    }
    response = client.post("/graphql", json=query)
    assert response.status_code == 200
    assert response.json() == {"data": {"hello": "Hello Tanuki 🦝"}}
