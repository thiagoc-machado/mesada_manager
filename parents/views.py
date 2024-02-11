from django.shortcuts import render
from django.contrib.auth.models import User
from .permissions import admin_or_staff_required


@admin_or_staff_required
def parents(request):
    

    return render(request, 'parents.html')
