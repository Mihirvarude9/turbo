"""
Run with:
    uvicorn turbo_app:app --host 0.0.0.0 --port 7865
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

API_KEY = "wildmind_5879fcd4a8b94743b3a7c8c1a1b4"

app = FastAPI(title="Turbo-stub")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://www.wildmindai.com",
        "https://api.wildmindai.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptIn(BaseModel):
    prompt: str


@app.post("/turbo")
async def turbo_generate(req: Request, body: PromptIn):
    if req.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Bad key")

    # ── do your real inference here ─────────────────────────
    fake_url = "https://api.wildmindai.com/turbo/images/demo.png"
    return {"image_url": fake_url}


@app.get("/turbo/ping")
def ping():
    return {"status": "ok"}
