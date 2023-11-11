from pydantic import BaseModel


class Commnent(BaseModel):
    id: int
    content: str

class Post(BaseModel):
    author: str
    date: str
    title: str
    content: str
    id: int
    comments: list[Commnent]
    
post = Post(
    author="John Doe",
    date="2021-08-15",
    title="My first post",
    content="Hello world!",
    id=1,
    comments=[
        Commnent(id=1, content="Nice post!"),
        Commnent(id=2, content="I like it!"),
    ]
)

print(post.model_dump_json(indent=2))