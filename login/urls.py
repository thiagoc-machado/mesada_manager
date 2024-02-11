from django.urls import path
from . import views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.my_login, name="login"),
    path('sair/', views.sair, name="sair")
] 