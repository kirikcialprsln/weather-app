from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
]
