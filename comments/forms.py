from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Comment


User = get_user_model()


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=250,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'your comment...'
            }
        )
    )

    image = forms.ImageField(
        label='<i class="fas fa-camera"></i>',
        allow_empty_file=True,
        required=False
    )

    class Meta:
        model = Comment
        fields = (
            'image',
            'content'
        )
    
    def add_comment(self, user, discussion):
        self.instance.author = user
        self.instance.discussion = discussion
        self.instance.save()
