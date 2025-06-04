from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional
from bson import ObjectId


class QuestionType(str, Enum):
    TEXT = "text"
    MULTIPLE_CHOICE = "multiple_choice"
    FILE = "file"


@dataclass
class Question:
    id: str
    text: str
    type: QuestionType
    points: float
    order: int
    options: Optional[List[str]] = None  # For multiple choice
    correct_answers: Optional[List[str]] = None


@dataclass
class Assignment:
    id: ObjectId = field(default_factory=ObjectId)
    title: str = ""
    description: str = ""
    instructions: str = ""
    type: str = ""  # exam, homework, quiz
    course_id: str = ""
    due_date: datetime = field(default_factory=datetime.now)
    grace_period: int = 0  # Minutes of tolerance after due_date
    status: str = ""  # draft, published
    questions: List[Question] = field(default_factory=list)
    total_points: float = 0.0
    passing_score: float = 0.0  # Minimum score to pass
    submission_rules: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
