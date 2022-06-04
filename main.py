from fastapi import FastAPI, Response, status, HTTPException
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
async def get_post_by_id(post_id: str, response: Response):
    filtered_post = list(filter(lambda post: (str(post['id']) == post_id), posts))
    if len(filtered_post) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Couldn't find any posts that match the id: {post_id}")

    return {"post": filtered_post[0]}


@app.post('/posts')
async def add_post(new_post: Post, response: Response):
    if not new_post.is_published:
        new_id: str = str(uuid.uuid4())

        posts.append({"id": new_id, "title": new_post.title, "content": new_post.content})
        response.status_code = 201
        return {"post": {"id": new_id, "title": new_post.title, "content": new_post.content}}

    else:
        return {"message": "Post already published"}
