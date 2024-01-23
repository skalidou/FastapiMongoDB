from fastapi import FastAPI

from server.routes.article import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Article"], prefix="/article")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app!"}


app.post