from fastapi import APIRouter
from enum import Enum

class BookName(str, Enum):
    bible = "Bible2"
    hp = "HarryPotter"
    jttw = "Journey to the West"

api_book = APIRouter()

@api_book.get("/all")
async def books_get():
    return {"mesage:": "Hello show all books!"}

# 路径参数
# :int 定义参数类型，必须是int
@api_book.get("/{book_id}")
async def get_book_id(book_id:int):
    return {"book_id": book_id}

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
