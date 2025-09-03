from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto

# ---------------------------
# Grade Lifecycle (State)
# ---------------------------

class GradeState(Enum):
    PENDING = auto()
    SUBMITTED = auto()
    APPROVED = auto()

@dataclass
class GradeSubmission:
    student_id: str
    section_id: str
    grade: Optional[str] = None
    state: GradeState = GradeState.PENDING

    def submit(self, grade: str):
        if self.state != GradeState.PENDING:
            raise ValueError("Only pending grades can be submitted")
        self.grade = grade
        self.state = GradeState.SUBMITTED

    def approve(self):
        if self.state != GradeState.SUBMITTED:
            raise ValueError("Only submitted grades can be approved")
        self.state = GradeState.APPROVED

# ---------------------------
# Domain Entities
# ---------------------------

@dataclass
class Student:
    student_id: str
    name: str

@dataclass
class Section:
    section_id: str
    course_id: str
    instructor_id: str
    capacity: int
    enrolled_students: List[str] = field(default_factory=list)
    waitlist: List[str] = field(default_factory=list)

    def has_seat(self) -> bool:
        return len(self.enrolled_students) < self.capacity

    def add_student(self, student_id: str):
        if not self.has_seat():
            raise ValueError("No seats available")
        self.enrolled_students.append(student_id)

    def remove_student(self, student_id: str):
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)

@dataclass
class Faculty:
    faculty_id: str
    name: str
    department: str
    contact: str
    courses_teaching: List[str] = field(default_factory=list)  # section_ids

    def view_courses(self, sections: Dict[str, Section]) -> List[str]:
        """Return list of courses this faculty teaches."""
        result = []
        for sid in self.courses_teaching:
            sec = sections.get(sid)
            if sec:
                result.append(f"{sec.course_id}-{sid}: Enrolled {len(sec.enrolled_students)}/{sec.capacity}")
        return result or ["No courses assigned"]

    def view_enrolled_students(self, section_id: str, sections: Dict[str, Section], students: Dict[str, Student]) -> List[str]:
        """Return list of enrolled students for a section taught by this faculty."""
        if section_id not in self.courses_teaching:
            return ["Not authorized for this section."]
        sec = sections.get(section_id)
        if not sec:
            return ["Section not found."]
        return [f"{sid}: {students[sid].name}" for sid in sec.enrolled_students if sid in students]