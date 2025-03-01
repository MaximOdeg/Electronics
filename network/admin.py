from django.contrib import admin

from .models import NetworkNode, Supplier


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "supplier", "debt_to_supplier", "created_at")
    list_filter = ("city",)
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Clear debt to supplier"


admin.site.register(Supplier)
admin.site.register(NetworkNode, NetworkNodeAdmin)
