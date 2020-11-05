from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile


User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=256, help_text='Email required')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class UserPictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        picture = forms.ImageField(
        label='<i class="fas fa-camera"></i>',
        )
        fields = (
            'picture',
        )
