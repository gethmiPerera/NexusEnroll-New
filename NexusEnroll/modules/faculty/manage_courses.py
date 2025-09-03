from typing import Dict
from modules.faculty.faculty import Student, Section, Faculty, GradeSubmission, GradeState

# ---------------------------
# Faculty Actions
# ---------------------------

def approve_student(student: Student, section: Section) -> str:
    """Approve a student into a section (manual override if needed)."""
    if section.has_seat():
        section.add_student(student.student_id)
        return f"Student {student.name} approved into {section.course_id}-{section.section_id}"
    else:
        return "No seats available."

def reject_student(student: Student, section: Section) -> str:
    """Reject a student (remove from waitlist)."""
    if student.student_id in section.waitlist:
        section.waitlist.remove(student.student_id)
        return f"Student {student.name} rejected from waitlist of {section.course_id}-{section.section_id}"
    return "Student not found on waitlist."

def update_grades(submission: GradeSubmission, grade: str) -> str:
    """Submit or approve grades with lifecycle."""
    try:
        if submission.state == GradeState.PENDING:
            submission.submit(grade)
            return f"Grade submitted ({grade})"
        elif submission.state == GradeState.SUBMITTED:
            submission.approve()
            return "Grade approved."
        elif submission.state == GradeState.APPROVED:
            return "Grade already approved."
    except Exception as ex:
        return f"Error: {ex}"