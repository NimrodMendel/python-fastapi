from fastapi import FastAPI
from models import Post
import uuid

app = FastAPI()

posts = []


@app.get('/')
async def root():
    return {"message": "Hello"}


@app.get('/posts')
async def get_posts():
    return {"posts": posts}


@app.get('/posts/{post_id}')
async def get_post_by_id(post_id: str):
    return {"message": post_id}


@app.post('/posts')
async def add_post(new_post: Post):
    if not new_post.is_published:
        posts.append({"id": uuid.uuid4(), "title": new_post.title, "content": new_post.content})
        return {"post": {"id": uuid.uuid4(), "title": new_post.title, "content": new_post.content}}

    else:
        return {"message": "Post already published"}
