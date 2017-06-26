from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    If your custom user model is a simple subclass of AbstractUser, then you can extend these forms in the manner below.
    Ref. https://docs.djangoproject.com/en/1.11/topics/auth/customizing/
    """

    #def validate_email(self):    #TODO: Get this to work



    class Meta(UserCreationForm.Meta):

        email_recog = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        email = forms.RegexField(label=('email'), max_length=256, regex=email_recog)

        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    # class Meta(UserChangeForm.Meta):
    #     model = User
    #     fields = UserChangeForm.Meta.fields + ('handle',)