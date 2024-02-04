from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gigachat import GigaChat

app = FastAPI(title="Simple GigaChat")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GigaChatInput(BaseModel):
    prompt: str


class GigaChatOutput(BaseModel):
    answer: str


@app.get("/")
async def read_root(path: Optional[str] = ""):
    return FileResponse("/static/index.html")


@app.post("/gigachat", response_model=GigaChatOutput)
async def gigachat(
    json_data: GigaChatInput, authorization: Optional[str] = Header(None)
):
    if authorization:
        token = authorization.split(" ")[1]
    else:
        token = None
    answer = get_gigachat(token, json_data.prompt)
    if not answer:
        raise HTTPException(status_code=400, detail="No answer from GigaChat")
    return {"answer": answer}


def get_gigachat(client_secret, promt):
    with GigaChat(credentials=client_secret, verify_ssl_certs=False) as giga:
        response = giga.chat(promt)
        return response.choices[0].message.content
