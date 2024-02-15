from django.shortcuts import render
from django.contrib.auth.models import User
from .permissions import admin_or_staff_required
from django.utils import timezone
import locale

from users.models import Mesada, UserProfileInfo, Historico_mesada

@admin_or_staff_required
def parents(request):
    if request.method == 'POST':
        # Handle form submission here
        # You can access form data using request.POST.get('fieldname')
        # Perform the necessary actions and redirect back to the same page

        users = User.objects.filter(is_staff=False)
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        mes_atual = timezone.now().strftime('%B')
        userProfileInfo = UserProfileInfo.objects.all()
        mesada = Mesada.objects.all()

        context = {
            'users': users,
            'mes_atual': mes_atual,
            'userProfileInfo': userProfileInfo,
            'mesada': mesada,
        }
        return render(request, 'parents.html', context)

    else:
        users = User.objects.filter(is_staff=False)
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        mes_atual = timezone.now().strftime('%B')
        userProfileInfo = UserProfileInfo.objects.all()
        mesada = Mesada.objects.all()


    context = {
        'users': users,
        'mes_atual': mes_atual,
        'userProfileInfo': userProfileInfo,
        'mesada': mesada,
    }
    return render(request, 'parents.html', context)

