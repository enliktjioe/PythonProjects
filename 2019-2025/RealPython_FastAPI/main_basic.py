# main.py

from fastapi import FastAPI

app = FastAPI()

# @app.get("/items/{item_id}") # for example http://localhost:8000/items/3
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/users/me") # Order Matters: Put Fixed Paths First
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}