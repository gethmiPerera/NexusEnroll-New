# modules/student/enrollment.py

from modules.core.enrollment_logic import validate_enrollment
from modules.student.notifications import send_notification

def request_enrollment(student, course):
    """
    Handles student enrollment with full validation.
    """
    result = validate_enrollment(student, course)

    if result == "Approved":
        student.enrolled_courses.append(course)
        # Update schedule
        for day, start, end in course.schedule:
            if day not in student.schedule:
                student.schedule[day] = []
            student.schedule[day].append((start, end, course.code))
        message = f"Enrollment Confirmed for {course.code}"
    else:
        message = f"Enrollment Rejected for {course.code}: {result}"

    send_notification(student, message)
    return message

def drop_course(student, course):
    """
    Allows a student to drop an enrolled course.
    """
    if course in student.enrolled_courses:
        student.enrolled_courses.remove(course)
        # Remove from schedule
        for day in student.schedule:
            student.schedule[day] = [slot for slot in student.schedule[day] if slot[2] != course.code]
        message = f"Course {course.code} dropped successfully."
    else:
        message = f"Cannot drop {course.code}: not enrolled."

    send_notification(student, message)
    return message
