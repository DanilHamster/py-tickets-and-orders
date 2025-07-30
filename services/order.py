import datetime

from django.db import transaction
from django.db.models import QuerySet

from db.models import Order, User, Ticket, MovieSession


def create_order(
        tickets: list[dict],
        username: str,
        date: datetime = None
) -> None:
    user = User.objects.get(username=username)
    with transaction.atomic():
        order = Order.objects.create(user_id=user.id)
        if date:
            order.created_at = date
            order.save()
        Ticket.objects.bulk_create([
            Ticket(
                movie_session=MovieSession.objects.get(
                    id=ticket["movie_session"]
                ),
                row=ticket["row"],
                seat=ticket["seat"],
                order_id=order.id
            ) for ticket in tickets
        ])


def get_orders(username: str = None) -> QuerySet:
    if username:
        user = User.objects.get(username=username)
        return Order.objects.filter(user_id=user.id)
    return Order.objects.all()
