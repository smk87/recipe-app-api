from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = ((None, {'fields': ('email', 'password')}),
                 (_('personal_info'), {'fields': ('name',)}),
                 (_('permissions'), {
                  'fields': ('is_active', 'is_staff', 'is_superuser')}),
                 (_('important dates'), {'fields': ('last_login',)}))


admin.site.register(models.User, UserAdmin)
