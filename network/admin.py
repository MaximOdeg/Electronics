from django.contrib import admin

from network.models import NetworkNode


@admin.action(description="Очищение задолженности перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "level",
        "supplier",
        "debt",
        "created_at",
    )
    list_filter = (
        "city",
        "level",
        "country",
    )
    search_fields = (
        "name",
        "email",
    )
    actions = [clear_debt]
