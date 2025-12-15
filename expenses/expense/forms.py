from django import forms
from .models import Expenditure

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['title', 'amount', 'category', 'date', 'notes']