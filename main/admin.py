from django.contrib import admin
from .models import *


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession')


admin.site.register(GitInTouch, ContactAdmin)
admin.site.register(Service, ServiceAdmin)
