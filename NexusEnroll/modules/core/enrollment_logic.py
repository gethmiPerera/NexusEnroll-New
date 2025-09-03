# modules/core/enrollment_logic.py

def validate_enrollment(student, course):
    """
    Validates enrollment for prerequisites, capacity, and time conflicts.
    """
    # Prerequisite check
    for prereq in course.prerequisites:
        if prereq not in student.completed_courses:
            return f"Missing prerequisite: {prereq}"

    # Capacity check
    if len(course.enrolled_students) >= course.capacity:
        return "Course is full"

    # Time conflict check
    for day, start, end in course.schedule:
        if day in student.schedule:
            for s, e, _ in student.schedule[day]:
                if (start < e and end > s):
                    return f"Time conflict on {day} {start}-{end}"

    return "Approved"
