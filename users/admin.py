from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_active", "is_staff")
    list_filter = ("is_active", "is_staff")
    search_fields = ("email",)
