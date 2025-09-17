from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: int | None = None
    name: str
    username: str
    user_password: str
    
class DataUser(BaseModel):
    username: str
    user_password: str
