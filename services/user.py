from typing import Optional

from db.models import User


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> Optional[User]:
    return User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name or "",
        last_name=last_name or "",
    )


def get_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
) -> User:
    filters = {}
    if user_id:
        filters["pk"] = user_id
    if username:
        filters["username"] = username
    if password:
        filters["password"] = password
    if email:
        filters["email"] = email
    if first_name:
        filters["first_name"] = first_name

    return User.objects.get(**filters)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    user = User.objects.get(pk=user_id)
    if username:
        user.username = username
    if password:
        user.set_password(password)
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
