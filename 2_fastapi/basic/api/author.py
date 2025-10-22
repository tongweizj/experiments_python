from fastapi import APIRouter, Query
from typing import Annotated

# author 接口
# 专门用于尝试 fastapi如下功能
# - Query Parameters
api_author = APIRouter()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @api_author.get("/")
# async def author_home():
#     return {"mesage:": "Hi all author!"}

@api_author.get("/")
# basic version
# async def read_author(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Annotated + Query version
async def read_author(q: Annotated[str | None, Query(max_length=10)] = 'Hi'):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@api_author.get("/list")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Query 默认值、字符串验证
@api_author.get("/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
