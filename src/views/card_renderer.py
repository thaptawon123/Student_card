from html import escape
from pathlib import Path

from src.models.student_card import StudentCard


class CardRenderer:
    def __init__(self, card: StudentCard) -> None:
        self.card = card

    def render_html(self) -> str:
        student = self.card.student
        project_root = Path(__file__).resolve().parents[2]
        photo_path = student.photo_path
        if photo_path.is_absolute():
            try:
                photo_path = photo_path.relative_to(project_root)
            except ValueError:
                pass
        photo = escape(photo_path.as_posix(), quote=True)
        student_id = escape(student.student_id)
        full_name = escape(student.full_name_th)
        faculty = escape(student.faculty)
        english_name = escape(student.full_name_en or student.full_name_th)
        card_number = escape(self.card.card_number)
        valid_through = escape(self.card.valid_through)
        return f"""<!DOCTYPE html>
<html lang="th">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>บัตรนักศึกษา - {full_name}</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <main class="page-shell">
      <section class="id-card front" aria-label="ด้านหน้าบัตรนักศึกษา">
        <div class="top-orbit orbit-left"></div>
        <div class="top-orbit orbit-right"></div>
        <header class="brand-header">
          <div class="logo-wrap">
            <img src="assets/photos/Npru-logo.png" alt="ตรามหาวิทยาลัยราชภัฏนครปฐม">
          </div>
          <div class="brand-name">
            <h1>มหาวิทยาลัยราชภัฏนครปฐม</h1>
            <h2>NAKORN PATHOM RAJBHAT UNIVERSITY</h2>
          </div>
        </header>
        <div class="detail-grid">
          <div class="profile-block">
            <div class="photo-frame">
              <img src="{photo}" alt="รูปนักศึกษา {full_name}" class="student-photo">
            </div>
          </div>
          <div class="info-block">
            <div class="field-row"><span class="label">ชื่อ-สกุล</span><span class="value">: {full_name}</span></div>
            <div class="field-row"><span class="label">รหัสนักศึกษา</span><span class="value">: {student_id}</span></div>
            <div class="field-row"><span class="label">สาขาวิชา</span><span class="value">: {faculty}</span></div>
            <div class="id-number-wrap"><span class="id-number">{card_number}</span></div>
            <div class="student-name-row">
              <div class="name-badge">{english_name}</div>
              <div class="chip-row"><span class="chip">VALID</span><span class="chip small">THRU {valid_through}</span></div>
            </div>
          </div>
          <div class="visa-block">
            <div class="visa-logo"><span class="visa-text">VISA</span><div class="visa-ring ring-1"></div><div class="visa-ring ring-2"></div></div>
          </div>
        </div>
        <div class="footer-row"><span>บัตรประจำตัวนักศึกษา</span></div>
      </section>
      <section class="id-card back" aria-label="ด้านหลังบัตรนักศึกษา">
        <div class="back-strip"></div>
        <div class="barcode-wrap"><div class="barcode" aria-label="บาร์โค้ด"></div></div>
      </section>
    </main>
  </body>
</html>
"""

    def write_html(self, output_path: Path) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(self.render_html(), encoding="utf-8")
        return output_path
