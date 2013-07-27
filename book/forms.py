from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from book.models import Verification, Transaction

class VerificationForm(forms.ModelForm):

    class Meta:
        model = Verification


VerificationTransactionFormSet = inlineformset_factory(
	Verification,
	Transaction,
)