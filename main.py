from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import model.base
from config.database import engine, SessionLocal
from dto.user import UserCreateRequest, UserResponse
from service import user_service

model.base.BaseTable.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/users", response_model=UserResponse)
def create_user(dto: UserCreateRequest, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, dto.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User with the email already registered")
    return user_service.create_user(db, dto)


@app.get("/api/users", response_model=List[UserResponse])
def get_user_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user_detail(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
