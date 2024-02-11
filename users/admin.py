from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfileInfo, Mesada, Historico_mesada




# Crie um InlineModelAdmin para a sua nova model
class UserProfileInfoInline(admin.StackedInline):  # Você pode usar também admin.TabularInline para um layout mais compacto
    model = UserProfileInfo
    extra = 1  # O número de formulários vazios exibidos na página de edição


# Substitua a classe UserAdmin padrão para incluir a sua nova model
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInfoInline]


# Registre a nova UserAdmin
admin.site.unregister(User)  # Desregistre o UserAdmin padrão
admin.site.register(User, CustomUserAdmin)

# Registre suas outras models
admin.site.register(Mesada)
admin.site.register(Historico_mesada)
