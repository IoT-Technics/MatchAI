from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.repositories.user import create_user, get_user_by_email
from app.schemas.auth import LoginRequest, RegisterRequest


class RegistrationError(Exception):
    """Raised when an authentication operation cannot be completed."""


def normalize_email(email: str) -> str:
    """Normalize an email address before persistence and lookup."""
    return email.strip().lower()


def register_user(
    db: Session,
    request: RegisterRequest,
):
    email = normalize_email(str(request.email))

    existing_user = get_user_by_email(db, email)

    if existing_user is not None:
        raise RegistrationError(
            "A user with this email already exists."
        )

    hashed_password = hash_password(request.password)

    return create_user(
        db,
        email=email,
        hashed_password=hashed_password,
        full_name=request.full_name.strip(),
        role=request.role,
    )


def authenticate_user(
    db: Session,
    request: LoginRequest,
) -> str:
    """Authenticate a user and return a JWT access token."""

    email = normalize_email(str(request.email))

    user = get_user_by_email(db, email)

    if user is None:
        raise RegistrationError("Invalid email or password.")

    if not user.is_active:
        raise RegistrationError("Invalid email or password.")

    if not verify_password(
        request.password,
        user.hashed_password,
    ):
        raise RegistrationError("Invalid email or password.")

    return create_access_token(
        subject=user.email,
        user_id=user.id,
        role=user.role,
    )