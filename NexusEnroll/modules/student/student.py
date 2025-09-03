# modules/student/student.py

class Student:
    """
    Represents a student in NexusEnroll.
    """

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []       # List of Course objects
        self.completed_courses = {}      # {Course code: grade}
        self.schedule = {}               # {day: [(time_start, time_end, course_code)]}

    def view_profile(self):
        """
        Displays student's profile and academic info.
        """
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Enrolled Courses:", [c.code for c in self.enrolled_courses])
        print("Completed Courses & Grades:", self.completed_courses)

    def view_enrolled_courses(self):
        """
        Displays currently enrolled courses.
        """
        if not self.enrolled_courses:
            print("No courses enrolled.")
        else:
            print("Currently Enrolled Courses:")
            for course in self.enrolled_courses:
                print(f"- {course.code}: {course.name}")

    def view_schedule(self):
        """
        Displays a simple calendar-like view of schedule.
        """
        print("Schedule:")
        for day, slots in self.schedule.items():
            print(f"{day}:")
            for start, end, course in slots:
                print(f"  {start}-{end}: {course}")

    def view_academic_progress(self, degree_requirements):
        """
        Displays completed courses and remaining required courses.
        """
        print("Completed Courses:")
        for code, grade in self.completed_courses.items():
            print(f"  {code}: {grade}")
        remaining = [course for course in degree_requirements if course not in self.completed_courses]
        print("Remaining Required Courses:", remaining)
