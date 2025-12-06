from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tobefair_backend.service.routes.check_app_routes import check_app_router
from tobefair_backend.service.routes.configuration_routes import configuration_router
from tobefair_backend.service.routes.evaluation_routes import evaluation_router
from tobefair_framework.core.notification.notifications_middleware import (
    NotificationMiddleware,
)

FAIR_TEAM = [
    {"name": "Leonardo Guerreiro Azevedo", "email": "lga@br.ibm.com"},
]

# TODO: Discover how to include more than one contact in the fast api contact info.
app = FastAPI(
    title="2BFAIR-backend",
    version="0.0.1",
    contact={
        "name": "Leonardo Guerreiro Azevedo",
        "url": "http://ibm.biz/leonardo",
        "email": "lga@br.ibm.com",
    },
)


origins = [
    "http://localhost:4200",
    "http://localhost:42000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(NotificationMiddleware)

app.include_router(evaluation_router)
app.include_router(configuration_router)
app.include_router(check_app_router)
