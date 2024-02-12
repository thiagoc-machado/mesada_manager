from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import locale

from django.contrib.auth.models import User
from users.models import Mesada, UserProfileInfo, Historico_mesada

@login_required
def kids(request):
    user = request.user
    try: 
        mesada_valor = UserProfileInfo.objects.get(user=user).valor_mesada
        mesadas_do_mes = Mesada.objects.filter(usuario=user, data_criacao__month=timezone.now().month)
        mesada_total = sum(mesada_valor + mesada.acrescimos - mesada.descontos for mesada in mesadas_do_mes)
        nome_mesadas = [mesada.nome for mesada in mesadas_do_mes]
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        mes_atual = timezone.now().strftime('%B')


        context = {
            'mes_atual': mes_atual,
            'user': user,
            'mesada_valor': mesada_valor,
            'nome_mesadas': nome_mesadas,
            'mesadas_do_mes': mesadas_do_mes,
            'mesada_total': mesada_total,
        }
    except Mesada.DoesNotExist:
        context = {
            'user': user,
            'mesadas_do_mes': None,  # Ou pode deixar vazio dependendo do que deseja na template
            'mesada_total': 0,
        }
    
    return render(request, 'kids.html', context)
