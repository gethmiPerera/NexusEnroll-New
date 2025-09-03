from dataclasses import dataclass, field
from typing import List, Set, Optional


@dataclass(frozen=True)
class Meeting:
    """Immutable meeting schedule for a section"""
    day_of_week: str
    start_time: str   # stored as "HH:MM"
    end_time: str
    location: str


@dataclass
class Course:
    course_id: str
    code: str
    name: str
    description: str
    department: str
    credits: int
    prerequisites: List[str] = field(default_factory=list)


@dataclass
class Section:
    section_id: str
    course_id: str
    term: str
    instructor_id: str
    capacity: int
    enrolled_count: int = 0
    meetings: List[Meeting] = field(default_factory=list)
    waitlist: List[str] = field(default_factory=list)

    def has_seat(self) -> bool:
        return self.enrolled_count < self.capacity

    def increment_enrolled(self):
        if not self.has_seat():
            raise ValueError("Section is at capacity")
        self.enrolled_count += 1

    def decrement_enrolled(self):
        if self.enrolled_count <= 0:
            raise ValueError("No students to remove")
        self.enrolled_count -= 1


@dataclass
class Student:
    student_id: str
    name: str
    program_id: str
    preferred_channel: str
    completed_courses: Set[str] = field(default_factory=set)
    current_enrollments: Set[str] = field(default_factory=set)


@dataclass
class Faculty:
    faculty_id: str
    name: str
    department: str
    email: str
    phone: str
    courses_taught: List[str] = field(default_factory=list)