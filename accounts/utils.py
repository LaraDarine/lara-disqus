from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import token_generator


def send_email_confirmation(request, user):
    token = token_generator.make_token(user)
    current_site = get_current_site(request)
    user_id = user.id

    subject = 'Account confirmation'
    message = render_to_string(
        'registration/account-activation-email.html',
        {
            'user': user,
            'token': token,
            'current_site': current_site,
            'user_id': user_id
        }
    )

    user.email_user(subject, message)
