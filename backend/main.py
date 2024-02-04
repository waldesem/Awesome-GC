from typing import Union

from fastapi import FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
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
    question: str


class GigaChatOutput(BaseModel):
    answer: str


app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.post("/gigachat", response_model=GigaChatOutput, status_code=201)
async def gigachat(
    item: GigaChatInput, Authorization: Union[str, None] = Header(default=None)
):
    if Authorization:
        token = Authorization.split(" ")[1]
    else:
        token = None
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    answer = get_gigachat(token, item.question)
    if not answer:
        raise HTTPException(status_code=400, detail="No answer from GigaChat")
    return {"answer": answer}


def get_gigachat(client_secret, question):
    with GigaChat(credentials=client_secret, verify_ssl_certs=False) as giga:
        response = giga.chat(question)
        return response.choices[0].message.content
