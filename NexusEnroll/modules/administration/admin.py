# admin.py
from course_mgmt import CourseManager, ProgramManager
from reports import ReportGenerator

class AdministratorService:
    """Facade for administrator functions."""

    def __init__(self, course_repo, section_repo, program_repo, student_repo, faculty_repo):
        self.course_mgr = CourseManager(course_repo, section_repo)
        self.program_mgr = ProgramManager(program_repo)
        self.reporter = ReportGenerator(course_repo, section_repo, student_repo, faculty_repo)

    # Course Management
    def create_course(self, course_id, name, description, credits):
        return self.course_mgr.create_course(course_id, name, description, credits)

    def update_course(self, course_id, **kwargs):
        return self.course_mgr.update_course(course_id, **kwargs)

    def delete_course(self, course_id):
        return self.course_mgr.delete_course(course_id)

    # Program Management
    def add_program(self, program_id, name, requirements):
        return self.program_mgr.add_program(program_id, name, requirements)

    def update_program(self, program_id, **kwargs):
        return self.program_mgr.update_program(program_id, **kwargs)

    # Reporting
    def generate_capacity_report(self, semester, threshold=90):
        return self.reporter.generate_capacity_report(semester, threshold)

    def generate_faculty_workload(self, semester):
        return self.reporter.generate_faculty_workload(semester)

    def generate_course_popularity(self, semester):
        return self.reporter.generate_course_popularity(semester)
