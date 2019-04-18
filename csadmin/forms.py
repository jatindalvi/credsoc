from django import forms
from django.contrib.auth.models import User

from .models import Account
from .models import interests


class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'

class ShareDividendForm(forms.ModelForm):
    fsharedividend=forms.FloatField()
    class Meta:
        model=interests
        fields=('sharedividend',)

class CDDividendForm(forms.Form):
    fcddividend=forms.FloatField()

class LongLoanForm(forms.Form):
    flongloaninterest=forms.FloatField()

class EmergencyLoanForm(forms.Form):
    femergencylaoninterest=forms.FloatField()

class FDInterestForm(forms.Form):
    ffdinterest=forms.FloatField()
