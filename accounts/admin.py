from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add__form = CustomUserCreationForm
    form =CustomUserChangeForm
    add__fieldsets = UserAdmin.add__fieldsets + (
        ("None", {"fields": ("email", "role", "team")}),
    )
    fieldsets = UserAdmin.add__fieldsets + (
        ("None", {"fields": ("email", "role", "team")}),
    )
    list_display =[
        "username", "email", "last_name", "first_name",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
