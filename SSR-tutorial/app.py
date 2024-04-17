from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()

# Konfiguration des Jinja2Templates-Pfads
templates = Jinja2Templates(directory="./templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Kontext kann verwendet werden, um Daten an das Template zu übergeben
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hallo Welt!"})
