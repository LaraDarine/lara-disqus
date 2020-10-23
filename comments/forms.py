from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Comment


User = get_user_model()


class CommentForm(UserCreationForm):

    class Meta:
        model = Comment
        fields = (
            'discussion',
            'content',
            'likes',
            'dislikes'
        )
