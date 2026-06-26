from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.modules.tickets import crud, schemas


router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("", response_model=schemas.TicketResponse)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)


@router.get("", response_model=list[schemas.TicketResponse])
def list_tickets(status: str | None = None, priority: str | None = None, db: Session = Depends(get_db)):
    return crud.get_tickets(db, status, priority)

@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    return crud.get_stats(db)


@router.get("/{ticket_id}", response_model=schemas.TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.patch("/{ticket_id}/status", response_model=schemas.TicketResponse)
def update_status(ticket_id: int, payload: schemas.TicketUpdateStatus, db: Session = Depends(get_db)):
    ticket = crud.update_status(db, ticket_id, payload.status)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
