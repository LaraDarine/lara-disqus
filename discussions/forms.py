from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Discussion


User = get_user_model()

class DiscussionForm(UserCreationForm):

    class Meta:
        model = Discussion
        fields = (
            'content',
            'main_image',
            'demo_image',
            'likes',
            'dislikes'
        )
