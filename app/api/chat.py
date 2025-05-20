from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def hello():
    return {"message": "FastAPI 서버 연결 성공!"}
