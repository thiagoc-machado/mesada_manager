from django.urls import path
from . import views
from .views import fazer_backup
# decorador administrador



urlpatterns = [
    path('', fazer_backup, name='fazer_backup'),
]