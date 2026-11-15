def mark_attendance(status):
    if status not in ["Present", "Absent"]:
        return "Invalid Status"

    return status


def calculate_attendance(present, total):
    if total <= 0:
        return 0

    return (present / total) * 100


def check_attendance(percentage):
    if percentage >= 75:
        return "Eligible"

    return "Not Eligible"