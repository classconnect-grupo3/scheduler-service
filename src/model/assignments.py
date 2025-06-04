from datetime import datetime
from enum import Enum
from typing import List, Optional
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer,
    Float,
    ForeignKey,
    Enum as SQLEnum,
)
from sqlalchemy.orm import relationship
from src.database.db import Base


class QuestionType(str, Enum):
    TEXT = "text"
    MULTIPLE_CHOICE = "multiple_choice"
    FILE = "file"


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    instructions = Column(String)
    type = Column(String)  # exam, homework, quiz
    course_id = Column(String)
    due_date = Column(DateTime)
    grace_period = Column(Integer)  # Minutes of tolerance after due_date
    status = Column(String)  # draft, published
    total_points = Column(Float)
    passing_score = Column(Float)  # Minimum score to pass
    submission_rules = Column(String)  # Stored as JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
