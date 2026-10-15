from dataclasses import dataclass

from src.models.student import Student


@dataclass(frozen=True)
class StudentCard:
    student: Student
    card_number: str
    card_type: str = "STUDENT"
    valid_through: str = "1/67"

    def __post_init__(self) -> None:
        if not self.card_number.strip():
            raise ValueError("Card number must not be empty.")
        if self.card_type != "STUDENT":
            raise ValueError("Only STUDENT cards are supported.")
