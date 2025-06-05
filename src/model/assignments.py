from datetime import datetime
from enum import Enum
from typing import List, Optional
from bson import ObjectId


class QuestionType(str, Enum):
    TEXT = "text"
    MULTIPLE_CHOICE = "multiple_choice"
    FILE = "file"


class Question:
    def __init__(
        self,
        id: str,
        text: str,
        type: QuestionType,
        points: float,
        order: int,
        options: Optional[List[str]] = None,
        correct_answers: Optional[List[str]] = None,
    ):
        self.id = id
        self.text = text
        self.type = type
        self.options = options
        self.correct_answers = correct_answers
        self.points = points
        self.order = order

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "type": self.type,
            "options": self.options,
            "correct_answers": self.correct_answers,
            "points": self.points,
            "order": self.order,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class Assignment:
    def __init__(
        self,
        title: str = "",
        description: str = "",
        instructions: str = "",
        type: str = "",  # exam, homework, quiz
        course_id: str = "",
        due_date: datetime = None,
        grace_period: int = 0,  # Minutes of tolerance after due_date
        status: str = "",  # draft, published
        questions: List[Question] = None,
        total_points: float = 0.0,
        passing_score: float = 0.0,  # Minimum score to pass
        submission_rules: List[str] = None,
        _id: ObjectId = None,
        created_at: datetime = None,
        updated_at: datetime = None,
    ):
        self._id = _id or ObjectId()
        self.title = title
        self.description = description
        self.instructions = instructions
        self.type = type
        self.course_id = course_id
        self.due_date = due_date or datetime.now()
        self.grace_period = grace_period
        self.status = status
        self.questions = questions or []
        self.total_points = total_points
        self.passing_score = passing_score
        self.submission_rules = submission_rules or []
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "instructions": self.instructions,
            "type": self.type,
            "course_id": self.course_id,
            "due_date": self.due_date,
            "grace_period": self.grace_period,
            "status": self.status,
            "questions": [q.to_dict() for q in self.questions],
            "total_points": self.total_points,
            "passing_score": self.passing_score,
            "submission_rules": self.submission_rules,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        if data.get("_id"):
            data["_id"] = ObjectId(data["_id"])
        if data.get("questions"):
            data["questions"] = [Question.from_dict(q) for q in data["questions"]]
        # Convert string dates to datetime objects if needed
        for date_field in ["due_date", "created_at", "updated_at"]:
            if isinstance(data.get(date_field), str):
                data[date_field] = datetime.fromisoformat(
                    data[date_field].replace("Z", "+00:00")
                )
        return cls(**data)
