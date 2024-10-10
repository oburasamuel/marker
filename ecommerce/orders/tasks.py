from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def send_order_confirmation_email(order_id):
    order = Order.objects.get(id=order_id)
    send_mail(
        'Order Confirmation',
        f'Your order {order.id} has been placed successfully.',
        'no-reply@example.com',
        [order.user.email],
    )
