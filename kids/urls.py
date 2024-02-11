from django.urls import path
from . import views

urlpatterns = [
    path('', views.kids, name="kids"),
]