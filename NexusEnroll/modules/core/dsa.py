# modules/core/dsa.py

class Course:
    """
    Represents a course in NexusEnroll.
    """

    def __init__(self, code, name, prerequisites=None, instructor=None, capacity=30, schedule=None, description=""):
        self.code = code
        self.name = name
        self.prerequisites = prerequisites if prerequisites else []
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled_students = []    # List of Student objects
        self.schedule = schedule if schedule else []  # [(day, start_time, end_time)]
        self.description = description
