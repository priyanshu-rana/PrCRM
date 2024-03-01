from django.contrib import admin
from ..models.user import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
