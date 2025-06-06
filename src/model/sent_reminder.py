from sqlalchemy import Column, String, DateTime
from src.database.postgres_db import Base
from datetime import datetime

class SentReminder(Base):
    __tablename__ = "sent_reminders"

    assignment_id = Column(String, primary_key=True)
    reminder_type = Column(String, primary_key=True)  # "24h" o "1h"
    sent_at = Column(DateTime, default=datetime.now)
