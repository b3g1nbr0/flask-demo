# Prompt Generator Web (Flask)

Aplikasi web profesional untuk membuat prompt AI yang terstruktur, detail, dan mudah digunakan oleh semua kalangan.

## Fitur Utama
- Generator prompt AI profesional (Tujuan, Bahasa, Gaya, Detail)
- Tampilan responsif dengan Bootstrap 5
- Halaman: Home, Generator, About, Contact, Privacy Policy, Terms, 404
- Form validasi Flask-WTF
- Tombol copy hasil prompt

## Cara Menjalankan
1. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi (mode dev):
   ```bash
   flask --app app run
   ```

## Struktur Folder
```
app/
  __init__.py
  routes.py
  forms.py
  promptgen.py
  templates/
    base.html
    index.html
    generator.html
    about.html
    contact.html
    privacy.html
    terms.html
    404.html
  static/
    css/style.css
tests/
  test_app.py
requirements.txt
README.md
.gitignore
```

## Testing
```
pytest
```

## Hak Cipta
(c) 2026 b3g1nbr0. All rights reserved.
