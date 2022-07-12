from django.contrib.auth.views import LoginView
from django.shortcuts import render


class LoginPage(LoginView):
    template_name = 'accounts/login.html'
