from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from count_tokens import count_tokens

class CountTokensModel(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
)

@app.get("/")
def read_root():
    return "read root"

@app.post("/count-tokens/")
def count_tokens_in_contents(body: CountTokensModel, q: Union[str, None] = None):
    return {"count": count_tokens(body.text)}
