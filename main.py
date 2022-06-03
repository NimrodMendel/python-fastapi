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
    filtered_post = list(filter(lambda post: (str(post['id']) == post_id), posts))

    return {"post": filtered_post[0]}


@app.post('/posts')
async def add_post(new_post: Post):
    if not new_post.is_published:
        new_id: str = str(uuid.uuid4())

        posts.append({"id": new_id, "title": new_post.title, "content": new_post.content})
        return {"post": {"id": new_id, "title": new_post.title, "content": new_post.content}}

    else:
        return {"message": "Post already published"}
