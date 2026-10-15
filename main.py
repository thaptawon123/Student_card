from pathlib import Path

from src.models.student import Student
from src.services.card_service import CardService
from src.views.card_renderer import CardRenderer


def main() -> None:
    project_root = Path(__file__).resolve().parent
    student = Student(
        student_id="674259015",
        first_name_th="นาย ทับตะวัน",
        last_name_th="งามดี",
        first_name_en="Tubtawan",
        last_name_en="Ngamdee",
        faculty="วิศวกรรมซอฟต์แวร์",
        photo_path=project_root / "assets" / "photos" / "รูปนักศึกษา.jpg",
    )
    service = CardService()
    card = service.create_card(student, card_number="6742 5901 5")
    result = service.validate_card(card)
    if not result["is_valid"]:
        raise RuntimeError("; ".join(result["errors"]))

    output = CardRenderer(card).write_html(project_root / "student_card.html")
    print(f"สร้างบัตรแล้ว: {output}")
    print("ตรวจสอบข้อมูล: ผ่าน")


if __name__ == "__main__":
    main()
