from fastapi import FastAPI
from models import Post

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello"}


@app.get('/posts')
async def get_posts():
    return {"message": "No posts yet"}


@app.post('/posts')
async def add_post(new_post: Post):
    if not new_post.is_published:
        return {"title": new_post.title, "content": new_post.content}

    return {"message": "Post already published"}
