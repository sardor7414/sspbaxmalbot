from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Appeals)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'address', 'name', 'phone_number', 'content_appeal', 'type_appeal', 'created_at')
    list_display_links = ('company_name', )
    list_filter = ('company_name', 'address', 'name', 'type_appeal', 'created_at')
