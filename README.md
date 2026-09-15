# Sahil Sharma Tutoring — FastAPI Website

This is a Python-powered website using FastAPI + Jinja2 + HTML/CSS.

## 1. Install Python

Use Python 3.10+.

## 2. Create and activate a virtual environment

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the website

From the project root:

```bash
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000

## 5. Add your Calendly link

Open:

`app/main.py`

Find:

```python
"calendly_url": "https://calendly.com/",
```

Replace it with your actual Calendly event URL.

You can also change your name, lesson title and price in the same `SITE` dictionary.

## Project structure

```text
sahil_tutoring_fastapi/
├── app/
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── requirements.txt
└── README.md
```
