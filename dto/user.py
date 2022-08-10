from pydantic import BaseModel


class BaseOrmModel(BaseModel):
    class Config:
        orm_mode = True


class UserCreateRequest(BaseOrmModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class UserResponse(BaseOrmModel):
    id: int
    email: str

    class Config:
        orm_mode = True
