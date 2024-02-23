from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .permissions import admin_or_staff_required
from django.utils import timezone
import locale
from users.models import Mesada, UserProfileInfo, Historico_mesada

@admin_or_staff_required
def parents(request):
    if request.method == 'POST':
        users = User.objects.filter(is_staff=False)
        locale.setlocale(locale.LC_TIME, 'es_ES')
        mes_atual = timezone.now().strftime('%B')
        userProfileInfo = UserProfileInfo.objects.all()
        mesada = Mesada.objects.all()

        user_id = request.POST.get('user_id')
        valor = request.POST.get('valor')
        motivo = request.POST.get('motivo')
        firt_day_current_month = timezone.now().replace(day=1) + timezone.timedelta(days=32)
        last_day_current_month = firt_day_current_month.replace(day=1) - timezone.timedelta(days=1)

        if 'acrescimos' in request.POST:
            print("acrescimos")
            print("User ID:", user_id)
            print("Valor:", valor)
            print("Motivo:", motivo)

            Mesada.objects.create(
                user_id=user_id,
                acrescimos=float(valor),
                descontos=0,
                nome=motivo,
                data_criacao=timezone.now(),
                data_pagamento=last_day_current_month,
            )

        elif 'descontos' in request.POST:
            Mesada.objects.create(
                user_id=user_id,
                descontos=float(valor),
                acrescimos=0,
                nome=motivo,
                data_criacao=timezone.now(),
                data_pagamento=last_day_current_month,
            )

        elif 'details' in request.POST:
            print("details")
            print("User ID:", user_id)

        elif 'delete' in request.POST:
            print("delete")
            print("User ID:", user_id)

        elif 'edit' in request.POST:
            print("edit")
            print("User ID:", user_id)

            Mesada.objects.filter(id=user_id).update(
                acrescimos=float(valor),
                descontos=0,
                nome=motivo,
                data_criacao=timezone.now(),
                data_pagamento=last_day_current_month,
            )

        return redirect('parents')
    


    else:
        users = User.objects.filter(is_staff=False)
        locale.setlocale(locale.LC_TIME, 'es_ES')
        mes_atual = timezone.now().strftime('%B')
        userProfileInfo = UserProfileInfo.objects.all()
        mesada = Mesada.objects.all()

        user_totals = []
        for user in users:
            user_total_value = user.userprofileinfo.valor_mesada
            user_acrescimos = 0
            user_descontos = 0

            for mesada_instance in user.mesada_set.all():
                user_acrescimos += mesada_instance.acrescimos
                user_descontos += mesada_instance.descontos

            user_total_value += user_acrescimos - user_descontos

            user_totals.append({
                'user': user,
                'user_acrescimos': user_acrescimos,
                'user_descontos': user_descontos,
                'user_total_value': user_total_value,
            })

        context = {
            'user_totals': user_totals,
            'mes_atual': mes_atual,
        }
        return render(request, 'parents.html', context)



    # else:
    #     users = User.objects.filter(is_staff=False)
    #     locale.setlocale(locale.LC_TIME, 'es_ES')
    #     mes_atual = timezone.now().strftime('%B')
    #     userProfileInfo = UserProfileInfo.objects.all()
    #     mesada = Mesada.objects.all()

    #     # Calculate total value for each user
    #     user_totals = []
    #     for user in users:
    #         user_total_value = user.userprofileinfo.valor_mesada
    #         user_acrescimos = 0
    #         user_descontos = 0

    #         for mesada_instance in user.mesada_set.all():
    #             user_acrescimos += mesada_instance.acrescimos
    #             user_descontos += mesada_instance.descontos

    #         user_total_value += user_acrescimos - user_descontos

    #         user_totals.append({
    #             'user': user,
    #             'user_acrescimos': user_acrescimos,
    #             'user_descontos': user_descontos,
    #             'user_total_value': user_total_value,
    #         })

    #     context = {
    #         'user_totals': user_totals,
    #         'mes_atual': mes_atual,
    #     }
    #     return render(request, 'parents.html', context)

