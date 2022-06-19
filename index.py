from fastapi import FastAPI
from routes.index import posts

app = FastAPI()

app.include_router(posts)