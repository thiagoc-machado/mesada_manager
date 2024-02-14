from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import locale

from users.models import Mesada, UserProfileInfo, Historico_mesada

@login_required
def kids(request):
    user = request.user
    if user.is_staff:
        user = request.user
    else:
        user = request.user
    try: 
        mesada_valor = UserProfileInfo.objects.get(user=user).valor_mesada
        mesadas_do_mes = Mesada.objects.filter(usuario=user, data_criacao__month=timezone.now().month)
        mesada_subtotal = sum(mesada.acrescimos - mesada.descontos for mesada in mesadas_do_mes)
        mesada_total = mesada_subtotal + mesada_valor 
        nome_mesadas = [mesada.nome for mesada in mesadas_do_mes]
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        mes_atual = timezone.now().strftime('%B')


        context = {
            'user': user,
            'mes_atual': mes_atual,
            'mesada_valor': mesada_valor,
            'nome_mesadas': nome_mesadas,
            'mesadas_do_mes': mesadas_do_mes,
            'mesada_total': mesada_total,
        }
    except Mesada.DoesNotExist:
        context = {
            'user': user,
            'mesadas_do_mes': None, 
            'mesada_total': 0,
        }
    
    return render(request, 'kids.html', context)
