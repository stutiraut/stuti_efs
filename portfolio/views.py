from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum


now = timezone.now()
def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'portfolio/customer_edit.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('portfolio:customer_list')


@login_required
def stock_list(request):
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})


@login_required
def stock_new(request):
   if request.method == "POST":
       form = StockForm(request.POST)
       if form.is_valid():
           stock = form.save(commit=False)
           stock.created_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html',
                         {'stocks': stocks})
   else:
       form = StockForm()
       # print("Else")
   return render(request, 'portfolio/stock_new.html', {'form': form})

@login_required
def stock_edit(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   if request.method == "POST":
       form = StockForm(request.POST, instance=stock)
       if form.is_valid():
           stock = form.save()
           # stock.customer = stock.id
           stock.updated_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
   else:
       # print("else")
       form = StockForm(instance=stock)
   return render(request, 'portfolio/stock_edit.html', {'form': form})


@login_required
def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    stock.delete()
    return redirect('portfolio:stock_list')

@login_required
def investment_list(request):
    investments = Investment.objects.filter(recent_date__lte=timezone.now())
    return render(request, 'portfolio/investment_list.html',
                 {'investments': investments})

@login_required
def investment_new(request):
   if request.method == "POST":
       form = InvestmentForm(request.POST)
       if form.is_valid():
           investment = form.save(commit=False)
           investment.created_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(recent_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html',
                         {'investments': investments})
   else:
       form = InvestmentForm()
       # print("Else")
   return render(request, 'portfolio/investment_new.html', {'form': form})


@login_required
def investment_edit(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   if request.method == "POST":
       form = InvestmentForm(request.POST, instance=investment)
       if form.is_valid():
           investment = form.save()
           investment.updated_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(recent_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html', {'investments': investments})
   else:
       # print("else")
       form = InvestmentForm(instance=investment)
   return render(request, 'portfolio/investment_edit.html', {'form': form})


@login_required
def investment_delete(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   investment.delete()
   return redirect('portfolio:investment_list')

@login_required
def bond_list(request):
   bonds = Bond.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/bond_list.html', {'bonds': bonds})

@login_required
def bond_new(request):
   if request.method == "POST":
       form = BondForm(request.POST)
       if form.is_valid():
           bond = form.save(commit=False)
           bond.created_date = timezone.now()
           bond.save()
           bonds = Bond.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/bond_list.html',
                         {'bonds': bonds})
   else:
       form = BondForm()
       # print("Else")
   return render(request, 'portfolio/bond_new.html', {'form': form})

@login_required
def bond_edit(request, pk):
   bond = get_object_or_404(Bond, pk=pk)
   if request.method == "POST":
       form = BondForm(request.POST, instance=bond)
       if form.is_valid():
           bond = form.save()
           # stock.customer = stock.id
           bond.updated_date = timezone.now()
           bond.save()
           bonds = Bond.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/bond_list.html', {'bonds': bonds})
   else:
       # print("else")
       form = BondForm(instance=bond)
   return render(request, 'portfolio/bond_edit.html', {'form': form})

@login_required
def bond_delete(request, pk):
    bond = get_object_or_404(Bond, pk=pk)
    bond.delete()
    return redirect('portfolio:bond_list')



@login_required
def summary(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    stocks = Stock.objects.filter(customer=pk)
    investments = Investment.objects.filter(customer=pk)
    bonds = Bond.objects.filter(customer=pk)
    sum_purchase_price = Stock.objects.filter(customer=pk).aggregate(Sum('purchase_price'))
    sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value'))
    sum_purchase_price = Bond.objects.filter(customer=pk).aggregate(Sum('purchase_price'))
    return render(request, 'portfolio/summary.html', {'customers': customers,
                                                    'stocks': stocks,
                                                    'investments': investments,
                                                    'bonds': bonds,
                                                    'sum_purchase_price': sum_purchase_price,
                                                    'sum_recent_value': sum_recent_value,
                                                    'sum_purchase_price': sum_purchase_price,})
