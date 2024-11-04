from fastapi import APIRouter
from pydantic import BaseModel
from services.gpt import gpt_response
from typing import List
from  domain.DestructObject import DestructionObject

router = APIRouter()

class GPTAnswer(BaseModel):
    gpt_answer: str

class Objects(BaseModel):
    objects: List[DestructionObject]

@router.post("/gpt-answer", response_model=GPTAnswer)
def read_items(data: Objects):
    answer = gpt_response(data.objects)
    return {"gpt_answer": answer}

