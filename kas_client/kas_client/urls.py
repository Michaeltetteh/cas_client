from django.contrib import admin
from django.urls import path,include
from auth.urls import account_auth_urls

urlpatterns = [
    path('', include((account_auth_urls, 'auth'), namespace='auth')),
    path('admin/', admin.site.urls),
]
