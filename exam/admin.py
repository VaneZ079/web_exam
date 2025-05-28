from django.contrib import admin
from .models import Izexam
from django.contrib.auth.models import User

@admin.register(Izexam)
class IzexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'exam_date', 'create_date', 'is_public')
    search_fields = ('title', 'write_users__email')
    list_filter = ('is_public', 'create_date', 'exam_date')
    filter_horizontal = ('write_users',)