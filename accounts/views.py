from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.models import User
from .forms import SignUpForm, UserPictureForm
from .utils import send_email_confirmation
from .tokens import token_generator


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.is_active = False
            user.save()
            picture_form = UserPictureForm(
                request.POST,
                request.FILES,
                instance=user.profile)

        if picture_form.is_valid():
            send_email_confirmation(request, user)
            picture_form.save()

        context = {
            'user': user
        }
        return render(
            request,
            'registration/signup-success.html',
            context)
    else:
        user_form = SignUpForm()
        picture_form = UserPictureForm()

    context = {
        'user_form': user_form,
        'picture_form': picture_form,
        'text': {
            'title': 'Happy to have you among us!',
            'action': 'Register',
            'description': '''Please, fill
             this form to join us.'''
        }
    }
    return render(request, 'registration/signup.html', context)


def activate_email(request, user_id, token):
    user = get_object_or_404(User, pk=user_id)

    if token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad token')


def profile(request):
    context = {
        'current_user': request.user
    }
    return render(request, 'profile/profile.html', context)
