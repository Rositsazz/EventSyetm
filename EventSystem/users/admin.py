from django.contrib import admin

# Register your models here.
from .models import BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    readonly_fields = ('created_at',)
    list_filter = ('is_active',)
    search_fields = ['email', 'first_name', 'last_name']