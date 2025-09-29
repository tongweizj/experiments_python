from fastapi import FastAPI

# 启动web服务器
import uvicorn
app = FastAPI()

@app.get('/')
async def root():
    return {"mesage:": "Hello"}

if __name__ == '__main__':
    uvicorn.run("myapi:app", host="127.0.0.1", port=8080, reload=True)