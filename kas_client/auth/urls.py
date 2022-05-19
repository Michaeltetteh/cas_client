from django.urls import path
from . import views
import django_cas_ng.views

app_name = "auth"

account_auth_urls = [
    path('',views.HomeView.as_view(),name="home"),
    path('accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
]
