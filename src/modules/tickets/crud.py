"""
crud  логика по работе с бд
"""

from sqlalchemy.orm import Session

from src.modules.tickets import models, schemas


# Tickets
def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()


def get_tickets(db: Session, status=None, priority=None):
    query = db.query(models.Ticket)

    if status:
        query = query.filter(models.Ticket.status == status)

    if priority:
        query = query.filter(models.Ticket.priority == priority)

    return query.all()


def update_status(db: Session, ticket_id: int, status: str):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        return None

    ticket.status = status
    db.commit()
    db.refresh(ticket)
    return ticket


def get_stats(db: Session):
    total = db.query(models.Ticket).count()

    def count_by(field, value):
        return db.query(models.Ticket).filter(field == value).count()

    return {
        "total": total,
        "open": count_by(models.Ticket.status, "open"),
        "in_progress": count_by(models.Ticket.status, "in_progress"),
        "closed": count_by(models.Ticket.status, "closed"),
        "high_priority": count_by(models.Ticket.priority, "high"),
        "medium_priority": count_by(models.Ticket.priority, "medium"),
        "low_priority": count_by(models.Ticket.priority, "low"),
    }

# Reports
def get_last_tickets(db: Session, limit: int = 10):
    return (
        db.query(models.Ticket)
        .order_by(models.Ticket.created_at.desc())
        .limit(limit)
        .all()
    )
