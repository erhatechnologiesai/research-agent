from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import ResearchRequest, ResearchReport
from app.services.research_loop import execute_research_cycle

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def home():
    return {"agent": settings.PROJECT_NAME, "status": "ready"}

@app.post("/research", response_model=ResearchReport)
def run_research(req: ResearchRequest):
    if not req.topic.strip():
        raise HTTPException(status_code=400, detail="Research topic cannot be empty.")
    result = execute_research_cycle(req.topic, req.depth)
    return ResearchReport(**result)
