from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import Mesada, UserProfileInfo, Historico_mesada

@login_required
def kids(request):
    return render(request, 'kids.html')
