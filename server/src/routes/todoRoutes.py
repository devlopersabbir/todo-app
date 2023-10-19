from fastapi import APIRouter


router = APIRouter()


@router.get("/", tags=["GET TODOS"])
async def get_todo():
    return {
        "fuck": "us"
    }
