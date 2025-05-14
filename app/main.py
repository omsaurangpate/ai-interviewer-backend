import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="AI Interviewer API",
    description="Backend API for AI Interviewer platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to AI Interviewer API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
