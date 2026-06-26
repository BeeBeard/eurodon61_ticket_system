from fastapi import FastAPI
from src.api.v1 import router


APP = FastAPI(title="Ticket System")
APP.include_router(router, prefix="/api/v1")
