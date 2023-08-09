from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    url: str
    description: str

items = {
    1: {
        "name": "Book",
        "price": 9.99,
        "url": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "You can read it!"
    },
    2: {
        "name": "Headphones",
        "price": 249.99,
        "url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Listen to stuff!"
    },
    3: {
        "name": "Backpack",
        "price": 79.99,
        "url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Carry things around town!"
    },
    4: {
        "name": "Glasses",
        "price": 129.99,
        "url": "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Now you can see!"
    },
    5: {
        "name": "Cup",
        "price": 4.99,
        "url": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
        "description": "Drink anything with it!"
    },
    6: {
        "name": "Shirt",
        "price": 29.99,
        "url": "https://images.unsplash.com/photo-1581655353564-df123a1eb820?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=800&q=80",
        "description": "Wear it with style!"
    }
}

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items.get(item_id)

@app.post("/items/")
async def create_item(item: Item):
    items[item.id] = item.dict()
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.dict()
    return {"message": "Item has been updated successfully"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item has been deleted successfully"}
