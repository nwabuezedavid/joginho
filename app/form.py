# forms.py
from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class InterForm(forms.ModelForm):
    class Meta:
        model = intertransferx
        fields = "__all__"

class localForm(forms.ModelForm):
    class Meta:
        model = localtransferx
        fields = "__all__"

class loanForm(forms.ModelForm):
    class Meta:
        model = loanx
        fields = "__all__"

class benefitForm(forms.ModelForm):
    class Meta:
        model = benfitx
        fields = "__all__"
class depositForm(forms.ModelForm):
    class Meta:
        model = depositex
        fields = "__all__"
