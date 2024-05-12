import os

from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .api.v1.des_stats.views import des_router
from .api.v1.triple_des_stats.views import triple_des_router
from .api.app_status import status_router

app = FastAPI(
    title="3DES api",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    version=os.getenv("APP_VERSION", default="DEV"),
)


def create_app() -> FastAPI:
    app.include_router(status_router)
    app.include_router(des_router)
    app.include_router(triple_des_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
