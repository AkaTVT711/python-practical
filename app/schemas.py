from pydantic import BaseModel


class TaskBase(BaseModel):
    summary: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    username: str
    first_name: str
    last_name: str
    is_admin: bool
    is_active: bool


class User(UserBase):
    id: int
    username: str
    first_name: str
    last_name: str
    is_active: bool
    is_admin: bool
    tasks: list[Task] = []

    class Config:
        orm_mode = True
