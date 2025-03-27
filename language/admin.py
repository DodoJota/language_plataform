from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Teacher, Student

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'teacher')
    search_fields = ('user__username', 'user__email')
    list_filter = ('teacher',)
    fieldsets = (
        (None, {
            'fields': ('user', 'teacher')
        }),
    )

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
