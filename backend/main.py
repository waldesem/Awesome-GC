from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
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


class LoginInput(BaseModel):
    username: str
    password: str


class GigaChatInput(BaseModel):
    model: str
    question: str
    auth: str
    login: LoginInput


class GigaChatOutput(BaseModel):
    answer: str


app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")


@app.get("/")
async def index():
    return FileResponse("static/index.html")


"""Authenticate with GigaChat and get a response.

If 'auth' is passed, authenticate with the provided credentials. 
Otherwise, authenticate with the provided username and password.

Chat with the GigaChat model using the provided question. 
Return the first response from GigaChat. Raise an exception if no 
response is received.

Args:
  typo: Either 'auth' or any other value. 
  item: GigaChatInput object with credentials and question.

Returns:
  GigaChatOutput object with the GigaChat response.

Raises:
  HTTPException: If no response received from GigaChat.
"""
@app.post("/gigachat/{typo}", response_model=GigaChatOutput, status_code=201)

async def gigachat(typo: str, item: GigaChatInput):
    if typo == "auth":
        giga = GigaChat(
            model=item.model,
            credentials=item.auth,
            verify_ssl_certs=False,
        )
    else:
        giga = GigaChat(
            base_url="",
            user=item.login.username,
            password=item.login.password,
            verify_ssl_certs=False,
        )

    with giga:
        response = giga.chat(item.question)
        answer = response.choices[0].message.content
    if not answer:
        raise HTTPException(status_code=400)
    return {"answer": answer}
