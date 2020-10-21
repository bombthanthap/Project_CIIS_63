from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from ciis_app.models import *

def admin_home(request):
    return render(request,"admin_templates/home_content.html")
def add_financial(request):
    return render(request,"admin_templates/add_financial.html")


def staff_account(request):
    return render(request,"admin_templates/staff_account.html")

def add_admin(request):
    return render(request,"admin_templates/add_admin.html")


def add_admin_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        try:
            user=CustomUser.objects.create_user(username=email,password=password,email=email,last_name=last_name,first_name=first_name,user_type=1)
            
        except:
            messages.error(request,"Failed to Add Admin")
            return HttpResponseRedirect(reverse("add_admin"))
        else:
            user.save()
            messages.success(request,"Successfully Added Admin")
            return HttpResponseRedirect(reverse("add_admin"))


def add_financial_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=email,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.financials.address=address
            user.save()
            messages.success(request,"Successfully Added financial")
            return HttpResponseRedirect(reverse("add_financial"))
        except:
            messages.error(request,"Failed to Add financial")
            return HttpResponseRedirect(reverse("add_financial"))



def staff_account(request):
    financials=Financials.objects.all()
    adminciis=AdminCIIS.objects.all()
    return render(request,"admin_templates/staff_account.html",{"financials":financials,"adminciis":adminciis})

def edit_financial(request,financial_id):
    financial=Financials.objects.get(admin=financial_id)
    return render(request,"admin_templates/edit_financial.html",{"financial":financial,"id":financial_id})
def edit_financial_save(request,financial_id):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=financial_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=email
            user.save()
            
            financial_model=Financials.objects.get(admin=financial_id)
            financial_model.address=address
            financial_model.save()
            messages.success(request,"Successfully Edited Financial")
            return HttpResponseRedirect(reverse("edit_financial",kwargs={"financial_id":financial_id}))
        except:
            messages.error(request,"Failed to Edit Financial")
            return HttpResponseRedirect(reverse("edit_financial",kwargs={"financial_id":financial_id}))

