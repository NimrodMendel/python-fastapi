from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello"}


@app.get('/posts')
async def get_posts():
    return {"message": "No posts yet"}
