from django.shortcuts import render
from .forms import AcountForm, ChargeForm
from .models import Acount, Charge

# Create your views here.

def base_page(request):
    return render(request, 'main.html')

def create_account(request):
    if request.method == "POST":
        form = AcountForm(request.POST)
        if form.is_valid():
            form.save()
            form = AcountForm()
            return render(request, 'accounts.html', {'form':form, 'lst_account': Acount.objects.all()})
        else:
            pass
    else:
        form = AcountForm()
    return render(request, 'accounts.html', {'form':form, 'lst_account': Acount.objects.all()})

def create_charge(request, account_id):
    if request.method == "POST":
        form = ChargeForm(request.POST)
        if form.is_valid():
            charge = form.save(commit=False) #пока в базу не сохранякем
            charge.account = Acount.objects.get(id=account_id)
            account = Acount.objects.get(id=account_id)
            account.amount += charge.transaction
            account.save()
            charge.save()
            form = ChargeForm()
            return render(request, 'charges.html', {'form':form, 'lst_charges': Charge.objects.filter(account=account_id)})
        else:
            pass
    else:
        form = ChargeForm()
    return render(request, 'charges.html', {'form':form, 'lst_charges': Charge.objects.filter(account=account_id)})


