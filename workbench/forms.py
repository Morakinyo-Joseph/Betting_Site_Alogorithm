from django import forms
from pkg_resources import require
from .models import Slip


class SlipCreationForm(forms.ModelForm):
    class Meta:
        model = Slip
        fields = (
            'predict',
        )