from pydantic import BaseModel, EmailStr, UUID4

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

    is_superuser: bool = False

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str | None = None

class UserInDBBase(UserBase):
    id: UUID4

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str

