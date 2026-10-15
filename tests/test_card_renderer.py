from pathlib import Path

from src.models.student import Student
from src.models.student_card import StudentCard
from src.views.card_renderer import CardRenderer


def test_renderer_includes_student_details_and_assets() -> None:
    student = Student(
        "674259015",
        "นาย ทับตะวัน",
        "งามดี",
        "วิศวกรรมซอฟต์แวร์",
        Path("assets/photos/รูปนักศึกษา.jpg"),
    )
    html = CardRenderer(StudentCard(student, "6742 5901 5")).render_html()

    assert "นาย ทับตะวัน งามดี" in html
    assert "674259015" in html
    assert "assets/photos/Npru-logo.png" in html
    assert "assets/photos/รูปนักศึกษา.jpg" in html


def test_renderer_escapes_user_supplied_html() -> None:
    student = Student(
        "674259015",
        "นาย <script>",
        "ทดสอบ",
        "ซอฟต์แวร์",
        Path("photo.jpg"),
    )
    html = CardRenderer(StudentCard(student, "123")).render_html()

    assert "<script>" not in html
    assert "&lt;script&gt;" in html
