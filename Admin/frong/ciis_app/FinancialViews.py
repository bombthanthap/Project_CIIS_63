from django.shortcuts import render


def financial_home(request):
    return render(request,"financial_templates/home_content.html")