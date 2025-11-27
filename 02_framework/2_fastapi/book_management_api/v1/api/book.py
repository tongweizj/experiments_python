from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel
# book 接口
# 专门用于尝试 fastapi如下功能
# - request body

class BookName(str, Enum):
    bible = "Bible2"
    hp = "HarryPotter"
    jttw = "Journey to the West"

# data model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

api_book = APIRouter()

@api_book.get("/all")
async def books_get():
    return {"mesage:": "Hello show all books!"}

# 路径参数
# :int 定义参数类型，必须是int
@api_book.get("/{book_id}")
async def get_book_id(book_id:int):
    return {"book_id": book_id}


@api_book.put("/{book_id}")
async def update_book(book_id: int, item: Item):
    return {"book_id": book_id, **item.dict()}

@api_book.put("/q/{book_id}")
async def update_qbook(book_id: int, item: Item, q: str | None = None):
    result = {"book_id": book_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result



# 路径顺序
# 相同函数名没有关系，多模态
@api_book.get("/name/Bible")
async def read_book_name():
    return {"book_name_Bible": "Bible"}


@api_book.get("/name/{book_name}")
async def read_book_name(book_name: str):
    return {"book_name": book_name, "message": "It is a book!"}

# 用枚举类型限定合法输入
@api_book.get("/masterpiece/{book_name}")
async def read_book_name(book_name: BookName):
    if book_name is BookName.bible:
        return {"book_name": book_name, "message": "It is a goood book!"}

    if book_name.value == "HarryPotter":
        return {"book_name": book_name, "message": "It is a goood book!"}

@api_book.post("/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict