from fastapi import APIRouter
from pydantic import BaseModel

class Req(BaseModel):
    text: str

class Res(BaseModel):
    text: str
    title: str

router = APIRouter()

@router.post("/", response_model=Res)
async def create_summary(req: Req):
    # TODO: Implement summary logic
    return Res(text="要約例…", title="タイトル例")