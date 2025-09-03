from typing import Dict
from modules.student.student import Student
from modules.student.enrollment import request_enrollment, drop_course
from modules.core.dsa import Course
from modules.faculty.faculty import Faculty, Section, GradeSubmission
from modules.faculty.manage_courses import approve_student, reject_student, update_grades


# Demo / Test Run
# ---------------------------

def main():
    # Setup data
    students: Dict[str, Student] = {
        "S1": Student("S1", "Alice"),
        "S2": Student("S2", "Bob"),
    }

    sections: Dict[str, Section] = {
        "SEC1": Section("SEC1", "CS101", "F1", capacity=2),
    }

    faculty = Faculty("F1", "Dr. Lee", "CS", "lee@uni.edu", courses_teaching=["SEC1"])

    # Faculty views their courses
    print("== Faculty Courses ==")
    print(faculty.view_courses(sections))

    # Approve students
    print("\n== Approvals ==")
    print(approve_student(students["S1"], sections["SEC1"]))
    print(approve_student(students["S2"], sections["SEC1"]))
    print(approve_student(students["S2"], sections["SEC1"]))  # capacity exceeded

    # View enrolled students
    print("\n== Enrolled Students ==")
    print(faculty.view_enrolled_students("SEC1", sections, students))

    # Grade submissions
    print("\n== Grade Workflow ==")
    sub = GradeSubmission("S1", "SEC1")
    print(update_grades(sub, "A"))  # submit grade
    print(update_grades(sub, "A"))  # approve grade
    print(update_grades(sub, "A"))  # already approved

if __name__ == "__main__":
    main()