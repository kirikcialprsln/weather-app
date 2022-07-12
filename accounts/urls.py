from django.contrib.auth.decorators import login_required
from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', login_required(views.logout_view), name='logout'),
]
