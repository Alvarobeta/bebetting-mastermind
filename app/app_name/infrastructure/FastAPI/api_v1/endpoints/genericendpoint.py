from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def status():
    return {"message": "Hello World"}