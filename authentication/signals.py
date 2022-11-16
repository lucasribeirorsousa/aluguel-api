from django.dispatch import receiver
from .tasks import send_email_password

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    send_email_password.delay(
        "Recuperação de senha",
        reset_password_token.key,
        reset_password_token.user.email,
    )
