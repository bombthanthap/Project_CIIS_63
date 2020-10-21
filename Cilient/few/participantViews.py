from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ciis_app.models import CustomUser


def participant_home(request):
    return render(request,"participant_templates/participant_home.html")

def participant_payment_history(request):
    return render(request,"participant_templates/participant_payment_history.html")

def participant_payment(request):
    return render(request,"participant_templates/participant_payment.html")

def participant_upload_payment(request):
    return render(request,"participant_templates/participant_upload_payment.html")

def participant_edit_infomation(request):
    return render(request,"participant_templates/participant_edit_infomation.html")