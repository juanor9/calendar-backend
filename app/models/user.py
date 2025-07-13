from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str
    hashed_password: str
    is_active: bool = True
