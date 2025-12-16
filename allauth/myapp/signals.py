from allauth.account.signals import email_confirmed
from django.dispatch import receiver

@receiver(email_confirmed)
def email_confirmed_handler(request, email_address, **kwargs):
    print(email_address)
    print(type(email_address))

    user = email_address.user
    print(type(user))