from fastapi import APIRouter
from config.db import conn
from models.index import post_
from schemas.index import Post_
posts = APIRouter()


@posts.get("/article/")
async def read_data():
    return conn.execute(post_.select()).fetchall()

@posts.get("/article/{id}")
async def read_data(id : int ):
    return conn.execute(post_.select().where(post_.c.id == id)).fetchall()

@posts.get("/article/data/{Status}")
async def read_data(Status : str):
    return conn.execute(post_.select().where(post_.c.Status == Status)).fetchall()

@posts.post("/article/")
async def write_data( posts : Post_):
    conn.execute(post_.insert().values(
        Title = posts.Title,
        Content = posts.Content,
        Category = posts.Category,
        Status = posts.Status ))
    return conn.execute(post_.select()).fetchall()
    

@posts.put("/article/{id}")
async def update_data( id : int, posts : Post_):
    conn.execute(post_.update().values(
        Title = posts.Title,
        Content = posts.Content,
        Category = posts.Category,
        Status = posts.Status 
    ).where(post_.c.id == id))
    return conn.execute(post_.select()).fetchall()

@posts.put("/article/trash/{id}")
async def update_data( id : int):
    conn.execute(post_.update().values(
        Status = "trash"
    ).where(post_.c.id == id))
    return conn.execute(post_.select()).fetchall()

@posts.delete("/article/{id}")
async def delete_data(id : int):
    conn.execute(post_.delete().where(post_.c.id == id))
    return conn.execute(post_.select()).fetchall()
