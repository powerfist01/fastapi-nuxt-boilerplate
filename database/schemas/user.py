from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # Allows SQLAlchemy model conversion
