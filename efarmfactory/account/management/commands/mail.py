from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Send email'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        subject = 'welcome to GFG world'
        message = f'Hi, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['aalap.j@simformsolutions.com', ]
        send_mail( subject, message, email_from, recipient_list )
