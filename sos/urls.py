from django.urls import path
from sos import views

urlpatterns = [
    path('', views.sos, name='sos'),
]