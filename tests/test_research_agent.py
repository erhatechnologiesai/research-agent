import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestResearchAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_research_execution(self):
        res = self.client.post("/research", json={"topic": "Autonomous Multi-Agent Systems", "depth": "standard"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["topic"], "Autonomous Multi-Agent Systems")
        self.assertGreaterEqual(len(data["key_findings"]), 3)
        self.assertGreaterEqual(len(data["sources_consulted"]), 2)

if __name__ == "__main__":
    unittest.main()
