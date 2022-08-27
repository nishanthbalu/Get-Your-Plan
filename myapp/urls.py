"""project URL Configuration

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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_plan_settings_add', views.admin_plan_settings_add, name='admin_plan_settings_add'),
    path('admin_plan_settings_edit', views.admin_plan_settings_edit, name='admin_plan_settings_edit'),
    path('admin_plan_settings_view', views.admin_plan_settings_view, name='admin_plan_settings_view'),
    path('admin_plan_settings_delete', views.admin_plan_settings_delete, name='admin_plan_settings_delete'),



    path('architect_login', views.architect_login_check, name='architect_login'),
    path('architect_logout', views.architect_logout, name='architect_logout'),
    path('architect_home', views.architect_home, name='architect_home'),
    path('architect_details_add', views.architect_details_add, name='architect_details_add'),
    path('architect_changepassword', views.architect_changepassword, name='architect_changepassword'),
    path('architect_details_update', views.architect_details_update, name='architect_details_update'),

    path('architect_plans_add', views.architect_plans_add, name='architect_plans_add'),
    path('architect_plans_delete', views.architect_plans_delete, name='architect_plans_delete'),
    path('architect_plans_view', views.architect_plans_view, name='architect_plans_view'),

    path('architect_plan_details_add', views.architect_plan_details_add, name='architect_plan_details_add'),
    path('architect_plan_details_delete', views.architect_plan_details_delete, name='architect_plan_details_delete'),
    path('architect_plan_details_view', views.architect_plan_details_view, name='architect_plan_details_view'),

    path('architect_sales_master_view', views.architect_sales_master_view, name='architect_sales_master_view'),

    path('architect_plan_ratings_view', views.architect_plan_ratings_view, name='architect_plan_ratings_view'),

    path('architect_user_proposal_view', views.architect_user_proposal_view, name='architect_user_proposal_view'),
    path('architect_user_proposal_reply', views.architect_user_proposal_reply, name='architect_user_proposal_reply'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_plans_search', views.user_plans_search, name='user_plans_search'),
    path('user_plan_type_search', views.user_plan_type_search, name='user_plan_type_search'),
    path('user_architect_plan_details_view', views.user_architect_plan_details_view, name='user_architect_plan_details_view'),

    path('user_architect_search', views.user_architect_search, name='user_architect_search'),

    path('user_sales_master_add', views.user_sales_master_add, name='user_sales_master_add'),
    path('user_sales_master_view', views.user_sales_master_view, name='user_sales_master_view'),

    path('user_plan_ratings_add', views.user_plan_ratings_add, name='user_plan_ratings_add'),
    path('user_plan_ratings_view', views.user_plan_ratings_view, name='user_plan_ratings_view'),
    path('user_plan_ratings_view2', views.user_plan_ratings_view2, name='user_plan_ratings_view'),

    path('user_architect_proposal_add', views.user_architect_proposal_add, name='user_architect_proposal_add'),
    path('user_architect_proposal_view', views.user_architect_proposal_view, name='user_architect_proposal_view'),
    path('user_architect_proposal_delete', views.user_architect_proposal_delete, name='user_architect_proposal_delete'),

]
