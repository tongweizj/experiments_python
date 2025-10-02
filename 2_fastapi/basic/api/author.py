from fastapi import APIRouter

api_author = APIRouter()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @api_author.get("/")
# async def author_home():
#     return {"mesage:": "Hi all author!"}


@api_author.get("/list")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# 默认值
@api_author.get("/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
