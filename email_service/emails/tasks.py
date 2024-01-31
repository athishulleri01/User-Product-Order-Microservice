# email_service/email/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_email(email, product_name, quantity):
    subject = 'Order Confirmation'
    message = f'Thank you for your order of {quantity} {product_name}(s).'
    from_email = 'your@email.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
