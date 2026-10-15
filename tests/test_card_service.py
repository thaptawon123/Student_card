from pathlib import Path

from src.models.student import Student
from src.services.card_service import CardService


def test_service_creates_and_validates_card(tmp_path: Path) -> None:
    photo = tmp_path / "student.jpg"
    photo.write_bytes(b"photo")
    student = Student("674259015", "ทับตะวัน", "งามดี", "วิศวกรรมซอฟต์แวร์", photo)

    service = CardService()
    card = service.create_card(student)

    assert card.card_number == student.student_id
    assert service.validate_card(card)["is_valid"] is True
