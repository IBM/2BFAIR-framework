from fastapi import APIRouter

check_app_router = APIRouter()

TAG_FAIRNESS_EVALUATION = "Check app"


@check_app_router.get("/health")
async def check_app_health():
    return True
