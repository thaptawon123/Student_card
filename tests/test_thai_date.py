from datetime import date

from src.utils.thai_date import to_thai_date


def test_formats_date_in_thai_calendar() -> None:
    assert to_thai_date(date(2025, 1, 2)) == "2 มกราคม 2568"
