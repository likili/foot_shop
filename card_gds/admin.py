from django.contrib import admin
from card_gds.models import *




class CardsAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "is_active", "price"]
    list_display_links = ["name", "surname"]

    list_filter = ["is_active", "price"]
    
    search_fields = ["name", "surname"]

    list_editable = ["is_active"]
    
    readonly_fields = ["is_active"]

    save_as = True

    save_on_top = True
    
    
    fieldsets = [
        (None, {'fields': ["name", "surname", "price", "category", "is_active"]}),
        ('Прочие данные', {'fields': ["photo", "keywords", "description"],

                              'classes': ['collapse']}),
    ] 






admin.site.register(Cards, CardsAdmin)
admin.site.register(Partners)
admin.site.register(Baners)