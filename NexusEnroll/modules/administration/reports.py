# reports.py
import csv
import io

class ReportGenerator:
    """Generates admin reports (Capacity, Workload, Popularity)."""

    def __init__(self, course_repo, section_repo, student_repo, faculty_repo):
        self.course_repo = course_repo
        self.section_repo = section_repo
        self.student_repo = student_repo
        self.faculty_repo = faculty_repo

    def generate_capacity_report(self, semester, threshold):
        """Generate CSV report of sections ≥ threshold% capacity."""
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(["Course", "Section", "Capacity", "Enrolled", "% Full"])
        for sec in self.section_repo.all():
            if sec["semester"] == semester:
                percent = (sec["enrolled"] / sec["capacity"]) * 100
                if percent >= threshold:
                    writer.writerow([sec["course"], sec["id"], sec["capacity"], sec["enrolled"], f"{percent:.1f}%"])
        return buffer.getvalue().encode("utf-8")

    def generate_faculty_workload(self, semester):
        # Similar logic, group sections by faculty
        pass

    def generate_course_popularity(self, semester):
        # Count enrollments per course, return top-N
        pass
