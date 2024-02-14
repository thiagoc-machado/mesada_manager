from django.shortcuts import render
from django.contrib.auth.models import User
from .permissions import admin_or_staff_required
from django.utils import timezone
import locale

from users.models import Mesada, UserProfileInfo, Historico_mesada

@admin_or_staff_required
def parents(request):
    users = User.objects.filter(is_staff=False)
    mesadas = Mesada.objects.all()
    mesada_valor = UserProfileInfo.objects.get(user=request.user).valor_mesada
    locale.setlocale(locale.LC_TIME, 'pt_BR')
    mes_atual = timezone.now().strftime('%B')


    context = {
        'users': users,
        'mes_atual': mes_atual,
        'mesada_valor': mesada_valor,
    #     'nome_mesadas': nome_mesadas,
    #     'mesadas_do_mes': mesadas_do_mes,
    #     'mesada_total': mesada_total,
    }
    return render(request, 'parents.html', context)

