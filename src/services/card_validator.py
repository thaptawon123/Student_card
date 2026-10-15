from typing import TypedDict

from src.models.student_card import StudentCard


class CardValidationResult(TypedDict):
    is_valid: bool
    errors: list[str]
    warnings: list[str]


class CardValidator:
    def validate(self, card: StudentCard) -> CardValidationResult:
        errors: list[str] = []
        warnings: list[str] = []
        photo = card.student.photo_path

        if not photo.is_file():
            errors.append(f"ไม่พบไฟล์รูปนักศึกษา: {photo}")

        return {
            "is_valid": not errors,
            "errors": errors,
            "warnings": warnings,
        }
