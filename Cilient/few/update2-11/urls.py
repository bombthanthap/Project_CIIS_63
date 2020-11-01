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
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
  
    path('',views.showLoginPage,name="show_login"),

    path('get_user_details', views.GetUserDetails),
    path('doLogin',views.doLogin,name="do_login"),


    path('register',views.doRegister,name="doRegister"),
    path('register_save',views.register_save,name="register_save"),


#Admin
    #SuperAdmin
    path('add_author',AdminViews.add_author),
    path('manage_member_thai',AdminViews.manage_member_thai),
    path('manage_member_foreign',AdminViews.manage_member_foreign),
    path('member_author_account',AdminViews.member_author_account),
    path('member_participant_account',AdminViews.member_participant_account),
    path('member_upgrade',AdminViews.member_upgrade),
    path('member_downgrade',AdminViews.member_downgrade),
    path('account_approval',AdminViews.account_approval),

    path('manages',AdminViews.simple_upload,name="manages"),
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    path('add_financial',AdminViews.add_financial,name="add_financial"),
    path('add_financial_save',AdminViews.add_financial_save,name="add_financial_save"),
    path('add_admin',AdminViews.add_admin,name="add_admin"),
    path('add_admin_save',AdminViews.add_admin_save,name="add_admin_save"),
    path('staff_account',AdminViews.staff_account,name="staff_account"),

    path('edit_financial/<str:financial_id>',AdminViews.edit_financial,name="edit_financial"),
    path('edit_financial_save/<str:financial_id>', AdminViews.edit_financial_save,name="edit_financial_save"),
    path('edit_dataciis/<str:dataciis_id>',AdminViews.edit_dataciis,name="edit_dataciis"),
    path('edit_dataciis_save/<str:dataciis_id>', AdminViews.edit_dataciis_save,name="edit_dataciis_save"),


    #Financial
    path('financial_home',FinancialViews.financial_home,name="financial_home"), 

#Clint
    #Author
    path('author_home',authorViews.author_home,name="author_home"),
    path('author_add_paperid',authorViews.author_add_paperid,name="author_add_paperid"),
    path('author_addpaperid_save',authorViews.author_addpaperid_save,name="author_addpaperid_save"),

    path('author_payment_history',authorViews.author_payment_history,name="author_payment_history"),
    path('author_choose_paper',authorViews.author_choose_paper,name="author_choose_paper"),
    path('author_upload_payment',authorViews.author_upload_payment,name="author_upload_payment"),
    path('author_change_status',authorViews.author_change_status,name="author_change_status"),
    path('author_edit_infomation',authorViews.author_edit_infomation,name="author_edit_infomation"),



    #Participant
    path('participant_home',participantViews.participant_home,name="participant_home"),
    path('participant_payment_history',participantViews.participant_payment_history,name="participant_payment_history"),
    path('participant_payment',participantViews.participant_payment,name="participant_payment"),
    path('participant_upload_payment',participantViews.participant_upload_payment,name="participant_upload_payment"),
    path('participant_edit_infomation',participantViews.participant_edit_infomation,name="participant_edit_infomation"),

    


    path('new',participantViews.new,name="new"),
    path('new_save',participantViews.new_save,name="new_save"),
    
    path('participant_payment_2',participantViews.participant_payment_2,name="participant_payment_2"),
    #path('participant_payment_input',participantViews.participant_payment_input,name="participant_payment_input"),
    path('participant_payment_save',participantViews.participant_payment_save,name="participant_payment_save"),

    path('Logout',views.showLoginPage,name="Logout"),


]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)