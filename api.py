from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn
from correction import *
from In22Labs_NLP import *
from Word_Syn_Ant import *

app = FastAPI()

class correx(BaseModel):
    word: str

class syn_ant(BaseModel):
    word: str

class npp(BaseModel):
    param: dict

@app.get("/nlp-engine/correction/")
async def correct(word:correx):
    try:
        # Endpoint for word correction
        return {"status_code":200,
                "message": "Is this what you are looking for? --> ",
                "response": correction(word.word)}
    except:
        return { "status_code" : 431,
                "message" : "Not able to process your request."}

@app.get("/nlp-engine/synonym/")
async def syn(word:syn_ant):
    try:
        # Endpoint for word synonym lookup
        return {"status_code":200,
                "message": "The synonym for "+word.word+ " is --> ",
                "response": synonyms(word.word)}
    except:
        return { "status_code" : 431,
                "message" : "Not able to process your request."}

@app.get("/nlp-engine/antonym/")
async def ant(word:syn_ant):
    try:
        # Endpoint for word antonym lookup
        return {"status_code":200,
                "message": "The antonym for "+word.word+ " is --> ",
                "response": antonyms(word.word)}
    except:
        return { "status_code" : 431,
                "message" : "Not able to process your request."}

@app.get("/nlp-engine/")
async def nl(param:npp):
    try:
        # Endpoint for general NLP operations
        A = In22Labs_NLP(param.param)
        g = A.Home()
        return {"status_code":200,
                "message": "Here are the things you wanted ",
                "response": g}
    except:
        return { "status_code" : 431,
                "message" : "Not able to process your request."}

if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
