from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ciis_app.models import CustomUser
def admin_home(request):
    return render(request,"admin_templates/home_content.html")

def test(request):
    return render(request,"admin_templates/test.html")
def add_author(request):
    return render(request,"admin_templates/add_author.html")

def manage_member_thai(request):
    return render(request,"admin_templates/manage_member_thai.html")

def manage_member_foreign(request):
    return render(request,"admin_templates/manage_member_foreign.html")

def member_author_account(request):
    return render(request,"admin_templates/member_author_account.html")

def member_participant_account(request):
    return render(request,"admin_templates/member_participant_account.html")

def member_upgrade(request):
    return render(request,"admin_templates/member_upgrade.html")

def member_downgrade(request):
    return render(request,"admin_templates/member_downgrade.html")

def account_approval(request):
    return render(request,"admin_templates/account_approval.html")







def add_financial(request):
    return render(request,"admin_templates/add_financial.html")



def add_financial_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.financials.address=address
            user.save()
            messages.success(request,"Successfully Added financial")
            return HttpResponseRedirect(reverse("add_financial"))
        except:
            messages.error(request,"Failed to Add financial")
            return HttpResponseRedirect(reverse("add_financial"))
