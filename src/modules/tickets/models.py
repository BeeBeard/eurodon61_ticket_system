from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.shared.models.base_models import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    status = Column(String, default="open", index=True)
    priority = Column(String, default="medium", index=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
