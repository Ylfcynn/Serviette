from django.forms import ModelForm
from .models import RoBit


class CreateRoBitForm(ModelForm):

    class Meta:
        model = RoBit
        fields = ('name', 'description', 'solidity_code',)


class EditRoBitForm(ModelForm):

    class Meta:
        model = RoBit
        fields = ('name', 'description', 'solidity_code',)