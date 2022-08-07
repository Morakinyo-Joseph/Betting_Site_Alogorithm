from django import forms
from .models import Slip


# class SlipCreationForm(forms.ModelForm):
#     class Meta:
#         model = Slip
#         fields = (
#             'predict',
#         )

class GameEditForm(forms.ModelForm):
    class Meta:
        model = Slip
        fields = (
            "predict",
        )
