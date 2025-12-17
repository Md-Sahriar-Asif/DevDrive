from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "is_active",
                    "is_staff", "is_superuser", "last_login",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)