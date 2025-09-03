# modules/student/notifications.py

def send_notification(student, message):
    """
    Sends/logs a notification to the student.
    """
    print(f"[Notification] To: {student.name} ({student.student_id}) -> {message}")

#test
