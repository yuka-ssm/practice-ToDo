from fastapi import FastAPI

app = FastAPI()
print("aqa")

@app.get("/hello")
async def hello():
    return {"message": "hello world!"} 