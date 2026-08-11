from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User, UserRole
from app.models.user import User


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    """Return a user by email address."""
    statement = select(User).where(User.email == email)

    return db.scalar(statement)

def get_user_by_id(
    db: Session,
    user_id: int,
):
    return db.query(User).filter(User.id == user_id).first()


def create_user(
    db: Session,
    *,
    email: str,
    hashed_password: str,
    full_name: str,
    role: UserRole = UserRole.CANDIDATE,
) -> User:
    """Create and persist a new user."""

    user = User(
        email=email,
        hashed_password=hashed_password,
        full_name=full_name,
        role=role,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user