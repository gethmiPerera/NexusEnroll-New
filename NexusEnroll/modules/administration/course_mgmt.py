# coursemanagement.py
class CourseManager:
    """Handles course & section CRUD operations."""

    def __init__(self, course_repo, section_repo):
        self.course_repo = course_repo
        self.section_repo = section_repo

    def create_course(self, course_id, name, description, credits):
        course = {"id": course_id, "name": name, "description": description, "credits": credits}
        self.course_repo.save(course)
        return course

    def update_course(self, course_id, **kwargs):
        course = self.course_repo.get(course_id)
        if not course:
            raise ValueError(f"Course {course_id} not found")
        course.update(kwargs)
        self.course_repo.save(course)
        return course

    def delete_course(self, course_id):
        return self.course_repo.delete(course_id)


class ProgramManager:
    """Handles degree program management."""

    def __init__(self, program_repo):
        self.program_repo = program_repo

    def add_program(self, program_id, name, requirements):
        program = {"id": program_id, "name": name, "requirements": requirements}
        self.program_repo.save(program)
        return program

    def update_program(self, program_id, **kwargs):
        program = self.program_repo.get(program_id)
        if not program:
            raise ValueError(f"Program {program_id} not found")
        program.update(kwargs)
        self.program_repo.save(program)
        return program
