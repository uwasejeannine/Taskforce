# wallet/views.py
from django.shortcuts import render, redirect
from .models import Transaction, Budget
from .forms import TransactionForm, BudgetForm



def home(request):
    return render(request, 'home.html')

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def manage_budget(request):
    budgets = Budget.objects.all()
    return render(request, 'manage_budget.html', {'budgets': budgets})

def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_budget')
    else:
        form = BudgetForm()
    return render(request, 'add_budget.html', {'form': form})

def budget_report(request):
    budgets = Budget.objects.all()
    budget_totals = []
    for budget in budgets:
        spent = Transaction.objects.filter(category=budget.category).aggregate(Sum('amount'))['amount__sum'] or 0
        remaining = budget.amount - spent
        budget_totals.append({'budget': budget, 'spent': spent, 'remaining': remaining})
    return render(request, 'budget_report.html', {'budget_totals': budget_totals})