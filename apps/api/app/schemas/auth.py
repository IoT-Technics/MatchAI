from pydantic import BaseModel, EmailStr, Field

from app.models.user import UserRole


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=255)
    role: UserRole = UserRole.CANDIDATE


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: UserRole
    is_active: bool

    model_config = {
        "from_attributes": True,
    }