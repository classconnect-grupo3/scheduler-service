from repository.get_active_assignments import get_active_assignments
from utils.logger import setup_logger

logger = setup_logger()


def get_upcoming_assignments():
    """Fetch all published assignments that haven't expired yet."""
    logger.info("Fetching active assignments")
    active_assignments = get_active_assignments()
    assignments_to_remind = []

    if len(active_assignments) == 0:
        return assignments_to_remind

    logger.info(f"Processing {len(active_assignments)} active assignments")
    for assignment in active_assignments:
        assignments_to_remind.append(
            {
                "event_type": "assignment.reminder",
                "assignment_id": str(assignment._id),
                "course_id": assignment.course_id,
                "assignment_title": assignment.title,
                "assignment_due_date": assignment.due_date.isoformat(),
            }
        )

    return assignments_to_remind
