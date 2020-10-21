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
from django.urls import path,include
from ciis_system import settings
from django.conf.urls.static import static
from ciis_app import AdminViews, AuthorViews, FinancialViews, views




urlpatterns = [
    path('',views.showLoginPage,name="show_login"),
    path('dd',views.showIndex),
    path('get_user_details', views.GetUserDetails),
    path('doLogin',views.doLogin,name="do_login"),
    path('register',views.showRegister,name="register"),
    path('register_save',views.register_save,name="register_save"),
    
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


    
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    path('add_financial',AdminViews.add_financial,name="add_financial"),
    path('add_financial_save',AdminViews.add_financial_save,name="add_financial_save"),
    path('add_admin',AdminViews.add_admin,name="add_admin"),
    path('add_admin_save',AdminViews.add_admin_save,name="add_admin_save"),
    path('staff_account',AdminViews.staff_account,name="staff_account"),
    

    path('edit_financial/<str:financial_id>',AdminViews.edit_financial,name="edit_financial"),
    path('edit_financial_save/<str:financial_id>', AdminViews.edit_financial_save,name="edit_financial_save"),



    path('financial_home',FinancialViews.financial_home,name="financial_home"),   

    path('author_home',AuthorViews.author_home,name="author_home"),   





    path('Logout',views.showLoginPage)

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)