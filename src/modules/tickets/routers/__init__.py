from fastapi import APIRouter

from src.modules.tickets.routers import reports, tickets

router = APIRouter()
router.include_router(reports.router)
router.include_router(tickets.router)
