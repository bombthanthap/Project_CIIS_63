
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotModified
from django.contrib.auth import login, logout, logout
from ciis_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from django.contrib import messages
from ciis_app.models import *
from ciis_app import forms
from ciis_app.resource import DataCIISResource
from tablib.core import Dataset


def showLoginPage(request):
    return render(request,"login_page.html")

def showIndex(request):
    return render(request,"home.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == "2":
                return HttpResponseRedirect('/financial_home')
            elif user.user_type == "3":
                return HttpResponseRedirect('/author_home')
            elif user.user_type == "4":
                return HttpResponseRedirect('/participant_home')

            else:
                return HttpResponseRedirect(reverse("admin"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def Logout(request):
    logout(request)
    #แจ้งว่าlogoutแล้ว แก้ messageได้
    messages.info(request, "Logged out successfully!")
    return redirect('/')


def doRegister(request):
    return render(request,"register.html")


def register_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        title=request.POST.get("title")
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        phone_number=request.POST.get("phonenum")
        passport_id=request.POST.get("ppID")
        affiliation=request.POST.get("affiliation")
        country=request.POST.get("contrys")
        nationality=request.POST.get("nationality")
        status=request.POST.get("drone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")

        try:
            if password == cpassword:
                pw = password
                
            else:
                raise e
            
            if status == "Participant":
                status = "pp"
                u_type = 4
            else:
                if country == "thai":
                    status = "authorthai"
                    u_type = 3

                else:
                    status = "authorforeigner"
                    u_type = 3

            
            user = CustomUser.objects.create_user(username=email,password=password,email=email,last_name=last_name,first_name=first_name,user_type=u_type)
            
            if u_type == 3:
                user.authors.phoneno=phone_number
                user.authors.passportid=passport_id
                user.authors.affiliation=affiliation
                user.authors.country=country
                user.authors.nationality=nationality
                user.authors.status=status
            else:
                user.participants.phoneno=phone_number
                user.participants.passportid=passport_id
                user.participants.affiliation=affiliation
                user.participants.country=country
                user.participants.nationality=nationality
                user.participants.status=status
                

            user.save()

            messages.success(request,"Register Success")

            return HttpResponseRedirect(reverse("Logout"))

        except Exception as e:
            print(e)
            messages.error(request,"Failed")
            return HttpResponseRedirect(reverse("doRegister"))



