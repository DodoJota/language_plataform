from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_teacher')  # Exibe o nome do usuário e se é professor ou não
    list_filter = ('is_teacher',)  # Filtra os perfis por ser professor ou não
    search_fields = ('user__username',)  # Permite buscar pelo nome de usuário

    # Se você quiser permitir a edição do is_teacher diretamente no formulário de edição:
    fieldsets = (
        (None, {
            'fields': ('user', 'is_teacher')  # Exibe o campo 'is_teacher' no formulário
        }),
    )

# Registra o modelo Profile no admin
admin.site.register(Profile, ProfileAdmin)
