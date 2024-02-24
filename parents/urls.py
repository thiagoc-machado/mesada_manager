from django.urls import path
from . import views


urlpatterns = [
    path('', views.parents, name="parents"),
    path('add_user/<int:id>/', views.parents, name="parents"),
]