"""ciis_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ciis_system import settings
from django.conf.urls.static import static
from ciis_app import AdminViews, FinancialViews, views ,participantViews, authorViews


urlpatterns = [
  
    path('',views.showLoginPage),
    path('dd',views.showIndex),
    path('get_user_details', views.GetUserDetails),
    path('doLogin',views.doLogin),
    path('admin_home',AdminViews.admin_home),
    path('add_financial',AdminViews.add_financial,name="add_financial"),
    path('add_financial_save',AdminViews.add_financial_save,name="add_financial_save"),
    path('financial_home',FinancialViews.financial_home),

    path('register',views.doRegister),

#Clint
    #Author
    path('author_home',authorViews.auther_home),
    path('auther_add_paperid',authorViews.auther_add_paperid),
    path('auther_payment_history',authorViews.auther_payment_history),
    path('auther_choose_paper',authorViews.auther_choose_paper),
    path('auther_upload_payment',authorViews.auther_upload_payment),
    path('auther_change_status',authorViews.auther_change_status),
    path('auther_edit_infomation',authorViews.auther_edit_infomation),

    #Participant
    path('participant_home',participantViews.participant_home),
    path('participant_payment_history',participantViews.participant_payment_history),
    path('participant_payment',participantViews.participant_payment),
    path('participant_upload_payment',participantViews.participant_upload_payment),
    path('participant_edit_infomation',participantViews.participant_edit_infomation),
    
    path('Logout',views.showLoginPage)



]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)