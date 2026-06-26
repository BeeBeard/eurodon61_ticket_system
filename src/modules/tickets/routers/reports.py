from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.modules.tickets.crud import get_stats, get_last_tickets


templates = Jinja2Templates(directory="src/templates")


router = APIRouter(tags=["Ticket reports"])

@router.get("/report", response_class=HTMLResponse)
def report(
    request: Request,
    db: Session = Depends(get_db),
):
    stats = get_stats(db)
    tickets = get_last_tickets(db)

    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "stats": stats,
            "tickets": tickets,
        },
    )
