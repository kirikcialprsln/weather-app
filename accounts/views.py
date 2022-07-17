from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from accounts.models import User


class LoginPage(LoginView):
    template_name = 'accounts/login.html'


def logout_view(request):
    logout(request)
    return redirect('login')


def list_users(request):
    qs = User.objects.all()
    context = {
        "users": qs
    }
    return render(request, "accounts/list.html", context)
