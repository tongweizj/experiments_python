from fastapi import APIRouter

api_book = APIRouter()

@api_book.get("/all")
async def books_get():
    return {"mesage:": "Hello show all books!"}