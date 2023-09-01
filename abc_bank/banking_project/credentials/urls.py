from django.urls import path
from . import views

app_name = "credentials"


urlpatterns = [
    path('', views.redirection, name='redirection'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
