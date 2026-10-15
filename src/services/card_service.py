from src.models.student import Student
from src.models.student_card import StudentCard
from src.services.card_validator import CardValidationResult, CardValidator


class CardService:
    def __init__(self, validator: CardValidator | None = None) -> None:
        self._validator = validator or CardValidator()

    def create_card(
        self,
        student: Student,
        card_number: str | None = None,
        card_type: str = "STUDENT",
    ) -> StudentCard:
        number = card_number or student.student_id
        return StudentCard(student=student, card_number=number, card_type=card_type)

    def validate_card(self, card: StudentCard) -> CardValidationResult:
        return self._validator.validate(card)
