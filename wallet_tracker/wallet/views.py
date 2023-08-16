# # wallet/views.py
# from django.shortcuts import render, redirect
# from .models import Transaction, Budget
# from .forms import TransactionForm, BudgetForm



# def home(request):
#     return render(request, 'home.html')

# def transaction_list(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'transaction_list.html', {'transactions': transactions})

# def add_transaction(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction_list')
#     else:
#         form = TransactionForm()
#     return render(request, 'add_transaction.html', {'form': form})

# def manage_budget(request):
#     budgets = Budget.objects.all()
#     return render(request, 'manage_budget.html', {'budgets': budgets})

# def add_budget(request):
#     message = None
#     if request.method == 'POST':
#         form = BudgetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message = f"Budget for {form.cleaned_data['account']} added successfully!"
#             form = BudgetForm()
#     else:
#         form = BudgetForm()
#     return render(request, 'add_budget.html', {'form': form, 'message': message})
# def budget_list(request):
#     budgets = Budget.objects.all()
#     return render(request, 'budget_list.html', {'budgets': budgets})


# def budget_report(request):
#     budgets = Budget.objects.all()
#     budget_totals = []
#     for budget in budgets:
#         spent = Transaction.objects.filter(category=budget.category).aggregate(Sum('amount'))['amount__sum'] or 0
#         remaining = budget.amount - spent
#         budget_totals.append({'budget': budget, 'spent': spent, 'remaining': remaining})
#     return render(request, 'budget_report.html', {'budget_totals': budget_totals})


from django.shortcuts import render, redirect
from .models import Transaction, Budget,Subcategory
from django.db.models import Sum
from datetime import datetime, timedelta
from django.contrib import messages



def home(request):
    transactions = Transaction.objects.all()
    total_expenses = transactions.aggregate(Sum('amount'))['amount__sum']

    budgets = Budget.objects.all()
    total_budgets = budgets.aggregate(Sum('limit'))['limit__sum']

    # Check if total expenses exceed total budgets
    if total_expenses > total_budgets:
        messages.warning(request, "Oops!!! Dear client, the money you need for your expenses is above your budget.")

    return render(request, 'home.html', {'transactions': transactions, 'total_expenses': total_expenses, 'total_budgets': total_budgets})

def add_transaction(request):
    if request.method == 'POST':
        account_type = request.POST['account_type']
        amount = request.POST['amount']
        category_id = request.POST['category']
        category = Subcategory.objects.get(id=category_id)
        transaction = Transaction(account_type=account_type, amount=amount, category=category)
        transaction.save()
        return redirect('home')
    
    categories = Subcategory.objects.all()
    return render(request, 'add_transaction.html', {'categories': categories})

def set_budget(request):
    if request.method == 'POST':
        limit = request.POST['limit']
        budget = Budget(limit=limit)
        budget.save()
        return redirect('home')
    return render(request, 'set_budget.html')

def generate_report(request):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        transactions = Transaction.objects.filter(timestamp__range=(start_date, end_date))
        total_expenses = transactions.aggregate(Sum('amount'))['amount__sum']
        return render(request, 'report.html', {'transactions': transactions, 'total_expenses': total_expenses})
    return render(request, 'generate_report.html')

