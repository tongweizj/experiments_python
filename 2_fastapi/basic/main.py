from fastapi import FastAPI
from fastapi import Request
# 导入陆游
from api.book import api_book

# 启动web服务器
import uvicorn
app = FastAPI()

# tags 可选，提示
app.include_router(api_book, prefix="/book", tags=["book api"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run("myapi:app", host="127.0.0.1", port=8080, reload=True)