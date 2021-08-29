from django.contrib import admin
from django.urls import path, include
from UseAccout import views

urlpatterns = [
    path('Register', views.regster, name="Register"),
    path('Login', views.login),
    path('Logout', views.logout),

]
