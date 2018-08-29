from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order {}'.format(order.id)
    message = '{}, your order is successfully performed.\
               Order ID {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'admin@recycleProject.ru', [order.email])

    return mail_send
