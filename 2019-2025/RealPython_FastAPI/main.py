# main.py

from typing import Optional

from fastapi import Request, FastAPI
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    # price: float
    # price: str
    tax: Optional[float] = None

app = FastAPI()

# @app.post("/items/")
@app.post("/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# @app.post("/")
# async def root(arbitrary_json: JSONStructure = None):
#     return {"received_data": arbitrary_json}