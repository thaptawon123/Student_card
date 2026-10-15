from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Student:
    student_id: str
    first_name_th: str
    last_name_th: str
    faculty: str
    photo_path: Path
    first_name_en: str = ""
    last_name_en: str = ""

    def __post_init__(self) -> None:
        if len(self.student_id) != 9 or not self.student_id.isdigit():
            raise ValueError("Student ID must contain exactly 9 digits.")
        for field_name in ("first_name_th", "last_name_th", "faculty"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} must not be empty.")

    @property
    def full_name_th(self) -> str:
        return f"{self.first_name_th} {self.last_name_th}"

    @property
    def full_name_en(self) -> str:
        return f"{self.first_name_en} {self.last_name_en}".strip()
