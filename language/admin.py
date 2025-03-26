from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_teacher', 'professor')  # Mostra 'professor' na lista de perfis
    search_fields = ('user__username', 'user__email')  # Permite buscar por username e email do usuário
    list_filter = ('is_teacher',)  # Filtra por professores ou alunos
    fieldsets = (
        (None, {
            'fields': ('user', 'is_teacher', 'professor')  # Adiciona o campo professor no formulário de criação/edição
        }),
    )

admin.site.register(Profile, ProfileAdmin)
