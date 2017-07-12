from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    If your custom user model is a simple subclass of AbstractUser, then you can extend these forms in the manner below.
    Ref. https://docs.djangoproject.com/en/1.11/topics/auth/customizing/
    """


    class Meta(UserCreationForm.Meta):

        username = forms.CharField(max_length=256)

        email_recog = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        email = forms.RegexField(label=('email'), max_length=256, regex=email_recog)

        first_name = forms.CharField(max_length=256)

        last_name = forms.CharField(max_length=256)

        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'first_name', 'last_name', 'orbit_schema', )

    # class Meta(UserChangeForm.Meta):
    #     model = User
    #     fields = UserChangeForm.Meta.fields + ('handle',)


class CustomUserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'orbit_schema', )
        widgets = {
                   'username': forms.TextInput(attrs={'class': 'profile'}),

                  }

