from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user import create_user, get_user_by_email
from app.schemas.auth import RegisterRequest


class RegistrationError(Exception):
    """Raised when registration cannot be completed."""


def register_user(
    db: Session,
    request: RegisterRequest,
):
    email = request.email.lower().strip()

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