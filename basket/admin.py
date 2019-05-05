from django.contrib import admin
from basket.models import *


class BasketStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "is_active"]
    list_display_links = ["name", "surname"]

    list_filter = ["is_active"]

    search_fields = ["name", "surname"]

    list_editable = ["is_active"]

    save_as = True

    save_on_top = True

    fieldsets = [
        (None, {'fields': ["name", "surname", "is_active"]}),

    ]


admin.site.register(OrderItems)
admin.site.register(Order)

admin.site.register(BasketStatus, BasketStatusAdmin)
