
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, logout
from ciis_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from django.contrib import messages
from ciis_app.models import CustomUser
from ciis_app.forms import SignUp
from ciis_app import forms


def showLoginPage(request):
    return render(request,"login_page.html")
def showIndex(request):
    return render(request,"home.html")
def showRegister(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
    else:
        html = 'welcome for first time'
    return render(request, 'register.html',{'form': form})



def register_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=SignUp(request.POST)
        if form.is_valid():
           
            select=form.cleaned_data["select"]
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            nationality=form.cleaned_data["nationality"]    
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            ID_CARD_NO = form.cleaned_data["ID_CARD_NO"]
            try:
                user=CustomUser.objects.create_user(username=email,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.is_active = False
               
                user.authors.select=select
                user.authors.nationality=nationality
                user.authors.ID_CARD_NO=ID_CARD_NO
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
                    })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                        mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
            except:
                messages.error(request,"Failed")
                return redirect('/')
        else:
            form=SignUp(request.POST)
            return redirect('/')



def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect('/financial_home')
            elif user.user_type=="3":
                return HttpResponseRedirect('/author_home')
            else:
                return HttpResponseRedirect(reverse("/"))
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