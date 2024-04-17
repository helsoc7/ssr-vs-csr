from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS Middleware Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Entwicklungszwecke, sicherer in der Produktion einschränken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str

# Simulieren einer Datenbank
items_db = [Item(id=1, name="Apfel"), Item(id=2, name="Banane")]

@app.get("/items/")
async def read_items():
    return items_db

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = next((item for item in items_db if item.id == item_id), None)
    return item

