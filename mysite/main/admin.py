from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']

admin.site.register(models.About)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name']
    list_display_links = ['id', 'user_name']
    search_fields = ['user_name']