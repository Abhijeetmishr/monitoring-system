from typing import Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import database, schemas
from .model import models

app = FastAPI()

@app.post("/")
def create(detail: schemas.CreateBlogRequest, db: Session = Depends(database.get_db)):
    to_create = models.Blog (
        id = detail.id,
        title = detail.title,
        body = detail.body
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "create_id": to_create.id
    }
