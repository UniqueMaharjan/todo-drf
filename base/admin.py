from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'is_completed' ,'created_at')
    list_filter = ('title','is_completed','created_at')

admin.site.register(Todo,TodoAdmin)
