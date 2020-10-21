from django.shortcuts import render

def author_home(request):
    return render(request,"author_templates/home_content.html")