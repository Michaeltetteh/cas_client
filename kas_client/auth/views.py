from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import View

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse('<p>Welcome to successfully logged in.<br><a href="http://localhost:8001/accounts/logout">Logout</a></p>')
        return HttpResponseRedirect(reverse('auth:cas_ng_login'))