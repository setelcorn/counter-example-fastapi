from typing import Union
from fastapi import FastAPI
from count_tokens import count_tokens

app = FastAPI()

@app.get("/")
def read_root():
    return "read root"

@app.post("/count-tokens/")
def count_tokens_in_contents(contents: str, q: Union[str, None] = None):
    return {"count": count_tokens(contents)}
