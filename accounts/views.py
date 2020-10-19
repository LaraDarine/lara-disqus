from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.models import User
from .forms import SignUpForm, UserPictureForm


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()
            picture_form = UserPictureForm(
                request.POST,
                instance=user.profile)

            if picture_form.is_valid():
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
            'description': '''Please, take a moment and fill
             in this form to create your account.'''
        }
    }
    return render(request, 'registration/signup.html', context)
