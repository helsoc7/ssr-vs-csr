from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
class Item(BaseModel):
    id: int
    name: str
    quantity: int
    category: str


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
    quantity: int
    category: str

# Simulieren einer Datenbank
items_db = [
    Item(id=1, name="Apfel", quantity=3, category="Obst"),
    Item(id=2, name="Banane", quantity=5, category="Obst")
]

@app.get("/items/", response_model=List[Item])
async def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    if any(i.id == item.id for i in items_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    idx = next((index for index, i in enumerate(items_db) if i.id == item_id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[idx] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    idx = next((index for index, i in enumerate(items_db) if i.id == item_id), None)
    if idx is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db.pop(idx)
    return {"message": "Item deleted"}
