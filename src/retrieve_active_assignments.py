from repository.assignment_repository import get_active_assignments


def get_upcoming_assignments(hours_before_due):
    """Fetch assignments that are 'published' and due within the next X hours."""
    assignments = get_active_assignments(hours_before_due)
    assignments_to_remind = []
    for assignment in assignments:
        assignments_to_remind.append(
            {
                "event_type": "assignment.reminder",
                "assignment_id": str(assignment.id),
                "course_id": assignment.course_id,
                "assignment_title": assignment.title,
                "assignment_due_date": assignment.due_date.isoformat(),
            }
        )

    return assignments_to_remind
    
