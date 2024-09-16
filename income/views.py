from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Source,UserIncome
from django.core.paginator import Paginator
import json
from userpreferences.models import UserPreference
# Create your views here.
import datetime

@login_required(login_url='/authentication/login')
def index(request):
    source=Source.objects.all()
    income = UserIncome.objects.filter(owner=request.user)
    paginator = Paginator(income,5)
    page_number = request.GET.get('page')
    page_obj=Paginator.get_page(paginator,page_number)
    currency=UserPreference.objects.get(user=request.user).currency
    context={
        'income':income,
        'page_obj' : page_obj,
        'currency':currency
    }
    return render(request,'income/index.html',context)

def add_income(request):
    sources=Source.objects.all()
    context={
        'sources':sources,
        'values':request.POST
    }
    if request.method == "GET":
        return render(request,'income/add_income.html',context)
    if request.method == "POST":
        amount = request.POST['amount']
        if not amount:
            messages.error(request,"Amount is required")
            return render(request,'income/add_income.html',context)
        date=request.POST['income_date']        
        source=request.POST['source']        
        description=request.POST['description']    
        UserIncome.objects.create(owner=request.user,amount=amount,date=date,source=source,description=description)    
        messages.success(request,"income saved")
        return redirect('income')



def income_edit(request, id):
    income = UserIncome.objects.get(pk=id)
    sources=Source.objects.all()
    context={
        'income':income,
        'values':income,
        'sources':sources,
    }
    if request.method=='GET':
        return render(request,"income/edit-income.html",context)
    else:
        amount = request.POST['amount']
        if not amount:
            messages.error(request,"Amount is required")
            return render(request,'income/edit-income.html',context)
        date=request.POST['income_date']        
        source=request.POST['source']        
        description=request.POST['description']    
        income.owner=request.user
        income.amount=amount
        income.date=date
        income.source=source
        income.description=description
        income.save() 
        messages.success(request,"Record Updated")
        return redirect('income')
        
        messages.info(request,"Handling post form")
        return render(request,"income/edit-income.html",context)
    

def delete_income(request,id):
    income = UserIncome.objects.get(pk=id)
    income.delete()
    messages.success(request,"Record deleted")
    return redirect('income')

def search_income(request):
    if request.method=="POST":
        search_str=json.loads(request.body).get('searchText')
        income=UserIncome.objects.filter(
            amount__istartswith=search_str,
            owner=request.user) | UserIncome.objects.filter(
                date__istartswith=search_str,
                owner=request.user) | UserIncome.objects.filter(
                    description__icontains=search_str,
                    owner=request.user) | UserIncome.objects.filter(
                        source__icontains=search_str,
                        owner=request.user)
        data=income.values()
        return JsonResponse(list(data),safe=False)
    
def income_source_summary(request):
    today = datetime.date.today()
    six_months_ago= today - datetime.timedelta(days=180)
    income=UserIncome.objects.filter(
        date__gte=six_months_ago,date__lte=today,
        owner=request.user)
    finalrep = {}

    def get_source(income):
        return income.source
    def get_income_source_amount(source):
        amount =0
        filtered_by_source = income.filter(source=source)
        for item in filtered_by_source:
            amount+=item.amount
        return amount
    source_list=list(set(map(get_source,income)))
    for x in income:
        for y in source_list:
            finalrep[y] = get_income_source_amount(y)

    return JsonResponse({'income_source_data':finalrep},safe=False)    

def stats(request):
    return render(request,'income/stats.html')