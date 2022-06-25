from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Roles(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class Stores(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Roles]