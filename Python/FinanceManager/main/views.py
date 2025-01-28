from django.shortcuts import render, redirect
from .models import Transaction
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from django.db.models import Sum

# Create your views here.

def index(request):
    return render(request, "main/index.html")

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('/users/profile/')
    else:
        form = TransactionForm(user=request.user)
    return render(request, 'main/transaction_form.html', {'form': form})

@login_required
def reports(request):
    transactions = Transaction.objects.filter(user=request.user)
    income_total = Transaction.objects.filter(user=request.user, type=Transaction.INCOME).aggregate(total=Sum('amount'))['total'] or 0
    expense_total = Transaction.objects.filter(user=request.user, type=Transaction.EXPENSE).aggregate(total=Sum('amount'))['total'] or 0
    total_balance = income_total - expense_total
    return render(request, 'main/reports.html', {
        'transactions': transactions,
        'income_total': income_total,
        'expense_total': expense_total,
        'total_balance': total_balance
    })