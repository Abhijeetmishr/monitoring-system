from pydantic import BaseModel

class CreateBlogRequest(BaseModel):
    id: int
    title: str
    body: str