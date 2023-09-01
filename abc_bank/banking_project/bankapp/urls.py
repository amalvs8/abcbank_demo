from django.urls import path
from . import views

app_name = "bankapp"


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home/application', views.application, name='application'),
    path('application_detail', views.home, name='application_detail'),
    path('getBranch/', views.getBranch, name='getBranch'),

]
