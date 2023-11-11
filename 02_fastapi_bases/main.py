from fastapi import FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    author: str


# Create a FastAPI app instance
app = FastAPI()

# Sample data: a list of Post objects
posts = [
    Post(title="First Post", content="Content of the first post", author="Author 1"),
    Post(title="Second Post", content="Content of the second post", author="Author 2"),
    Post(title="Third Post", content="Content of the third post", author="Author 3")
]

# Define the endpoint
@app.get("/", tags=["posts"])
def list_all_posts():
    return {"articles": posts}