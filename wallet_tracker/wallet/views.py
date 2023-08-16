
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
        messages.warning(request, "N:B: Oops!!! Dear client, the money you need for your expenses is above your budget.")

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

