from repository.get_active_assignments import get_active_assignments
from utils.logger import setup_logger

logger = setup_logger()


def get_upcoming_assignments(hours_before_due):
    """Fetch assignments that are 'published' and due within the next X hours."""
    logger.info(f"Fetching assignments due in the next {hours_before_due} hours")
    active_assignments = get_active_assignments(hours_before_due)
    assignments_to_remind = []

    if len(active_assignments) == 0:
        logger.info("No active assignments found")
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

    logger.info(f"Created {len(assignments_to_remind)} reminder events")
    return assignments_to_remind
