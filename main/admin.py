from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as AuthGroupAdmin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import Group as AuthGroup
from django.contrib.auth.models import User as AuthUser


class AdminSite(admin.AdminSite):
    pass

admin_site = AdminSite()
admin_site.register(AuthUser, AuthUserAdmin)
admin_site.register(AuthGroup, AuthGroupAdmin)