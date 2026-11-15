from attendance import (
    mark_attendance,
    calculate_attendance,
    check_attendance
)


def test_mark_present():
    assert mark_attendance("Present") == "Present"


def test_mark_absent():
    assert mark_attendance("Absent") == "Absent"


def test_invalid_status():
    assert mark_attendance("Late") == "Invalid Status"


def test_attendance_percentage():
    assert calculate_attendance(18, 20) == 90


def test_eligible_student():
    assert check_attendance(80) == "Eligible"


def test_not_eligible_student():
    assert check_attendance(60) == "Not Eligible"


def test_zero_total_classes():
    assert calculate_attendance(0, 0) == 0