from django import forms
from .models import Transaction, Budget
from django.db.models import Sum


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'category', 'amount', 'description']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['account', 'category', 'maximum_amount']

    def clean_maximum_amount(self):
        maximum_amount = self.cleaned_data.get('maximum_amount')
        if maximum_amount is not None:
            # Retrieve the related budget category and calculate spent amount
            category = self.cleaned_data.get('category')
            spent = Transaction.objects.filter(category=category).aggregate(Sum('amount'))['amount__sum'] or 0

            if spent > maximum_amount:
                raise forms.ValidationError("Budget exceeded. You can't set a maximum amount lower than the already spent amount.")
        return maximum_amount
