from django.urls import path

from . import views

app_name = 'space_mailings'

urlpatterns = [
    path('', views.task, name='index'),
]