# main.py
from modules.student.student import Student
from modules.student.enrollment import request_enrollment, drop_course
from modules.core.dsa import Course

# ---------- Sample Data Initialization ----------
# Create some courses
course1 = Course(
    code="CS101",
    name="Introduction to Programming",
    prerequisites=[],
    instructor="Dr. Smith",
    capacity=2,
    schedule=[("Mon", 9, 11), ("Wed", 9, 11)],
    description="Learn the basics of programming in Python."
)

course2 = Course(
    code="CS201",
    name="Data Structures",
    prerequisites=["CS101"],
    instructor="Prof. Johnson",
    capacity=2,
    schedule=[("Tue", 10, 12), ("Thu", 10, 12)],
    description="Learn fundamental data structures and algorithms."
)

all_courses = [course1, course2]

# Create a student
student1 = Student("S100", "Alice")
student1.completed_courses = {"CS101": "A"}  # Completed course for prerequisite test

# ---------- Main Menu ----------
def browse_courses():
    print("\n--- Course Catalogue ---")
    for course in all_courses:
        seats_left = course.capacity - len(course.enrolled_students)
        print(f"{course.code} - {course.name}")
        print(f"  Instructor: {course.instructor}")
        print(f"  Description: {course.description}")
        print(f"  Seats: {seats_left}/{course.capacity}")
        print(f"  Schedule: {course.schedule}")
        print(f"  Prerequisites: {course.prerequisites}\n")

def enroll_course():
    code = input("Enter course code to enroll: ").strip()
    course = next((c for c in all_courses if c.code == code), None)
    if not course:
        print("Course not found.")
        return
    message = request_enrollment(student1, course)
    print(message)
    if "Confirmed" in message:
        course.enrolled_students.append(student1)

def drop_course_ui():
    code = input("Enter course code to drop: ").strip()
    course = next((c for c in all_courses if c.code == code), None)
    if not course:
        print("Course not found.")
        return
    message = drop_course(student1, course)
    print(message)
    if "dropped" in message:
        course.enrolled_students.remove(student1)

def main():
    while True:
        print("\n--- NexusEnroll Student Menu ---")
        print("1. Browse Courses")
        print("2. Enroll in a Course")
        print("3. Drop a Course")
        print("4. View Enrolled Courses")
        print("5. View Schedule")
        print("6. View Academic Progress")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            browse_courses()
        elif choice == "2":
            enroll_course()
        elif choice == "3":
            drop_course_ui()
        elif choice == "4":
            student1.view_enrolled_courses()
        elif choice == "5":
            student1.view_schedule()
        elif choice == "6":
            degree_requirements = ["CS101", "CS201", "CS301"]
            student1.view_academic_progress(degree_requirements)
        elif choice == "0":
            print("Exiting NexusEnroll. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
