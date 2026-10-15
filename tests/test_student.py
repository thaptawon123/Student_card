from pathlib import Path

import pytest

from src.models.student import Student


def make_student(student_id: str = "674259015") -> Student:
    return Student(
        student_id=student_id,
        first_name_th="นาย ทับตะวัน",
        last_name_th="งามดี",
        faculty="วิศวกรรมซอฟต์แวร์",
        photo_path=Path("assets/photos/รูปนักศึกษา.jpg"),
    )


def test_student_full_name() -> None:
    assert make_student().full_name_th == "นาย ทับตะวัน งามดี"


def test_student_id_must_have_nine_digits() -> None:
    with pytest.raises(ValueError, match="9 digits"):
        make_student("123")
