# -*- coding: utf-8 -*-

from typing import Optional
from fastapi import FastAPI

import bot

app = FastAPI()

@app.get("/")
def read_root():
    return {"ChatBot": "Hello World"}


@app.get("/msg/{text}")
def read_msg(text: str, q: Optional[str] = None):
    return bot.quest(text)
