from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Einbinden des statischen Verzeichnisses
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def main():
    return {"message": "Gehe zu /static/index.html für das CSR-Beispiel"}
