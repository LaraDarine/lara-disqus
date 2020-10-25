from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Comment


User = get_user_model()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'content',
            'image'
        )
    
    def add_comment(self, user, discussion):
        self.instance.author = user
        self.instance.discussion = discussion
        self.instance.save()
