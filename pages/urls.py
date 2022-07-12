from django.contrib.auth.decorators import login_required
from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', login_required(views.home), name='home'),
]
