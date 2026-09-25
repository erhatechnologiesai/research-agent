from pydantic import BaseModel
from typing import List, Dict

class ResearchRequest(BaseModel):
    topic: str
    depth: str = "standard"  # quick, standard, deep

class ResearchReport(BaseModel):
    topic: str
    key_findings: List[str]
    synthesis: str
    sources_consulted: List[Dict[str, str]]
    confidence_score: float
