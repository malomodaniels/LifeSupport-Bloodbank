from django import forms
from .models import Donor, Recipient

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"
