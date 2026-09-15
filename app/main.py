from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Sahil Sharma Tutoring")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

SITE = {
    "name": "Sahil Sharma",
    "lesson": "60-minute Mathematics Lesson",
    "price": "£30",
    # Replace this with your personal Calendly event link.
    "calendly_url": "https://calendly.com/",
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"site": SITE},
    )

@app.get("/health")
async def health():
    return {"status": "ok"}
