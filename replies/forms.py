from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Reply


User = get_user_model()


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = (
            'content',
        )
    
    def add_reply(self, user, comment):
        self.instance.author = user
        self.instance.comment = comment
        self.instance.save()
