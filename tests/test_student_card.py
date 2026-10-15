from pathlib import Path

import pytest

from src.models.student import Student
from src.models.student_card import StudentCard


def test_student_card_keeps_student_and_number() -> None:
    student = Student(
        "674259015",
        "นาย ทับตะวัน",
        "งามดี",
        "วิศวกรรมซอฟต์แวร์",
        Path("photo.jpg"),
    )
    card = StudentCard(student, "6742 5901 5")
    assert card.student is student
    assert card.card_number == "6742 5901 5"


def test_student_card_rejects_unsupported_type() -> None:
    student = Student(
        "674259015",
        "นาย ทับตะวัน",
        "งามดี",
        "วิศวกรรมซอฟต์แวร์",
        Path("photo.jpg"),
    )
    with pytest.raises(ValueError, match="Only STUDENT"):
        StudentCard(student, "123", card_type="OTHER")
