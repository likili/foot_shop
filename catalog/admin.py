from django.contrib import admin
from catalog.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "is_active", "is_index"]
    list_display_links = ["name", "surname"]

    list_filter = ["is_active", "is_index"]

    search_fields = ["name", "surname"]

    list_editable = ["is_active"]

    readonly_fields = ["is_active"]

    save_as = True

    save_on_top = True

    fieldsets = [
        (None, {'fields': ["name", "slug", "surname", "is_active"]}),
        ('Прочие данные', {'fields': ["photo", "indexsurname", "is_index"],

                           'classes': ['collapse']}),
    ]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "is_active"]
    list_display_links = ["name", "surname"]

    list_filter = ["is_active"]

    search_fields = ["name", "surname"]

    list_editable = ["is_active"]

    readonly_fields = ["is_active"]

    save_as = True

    save_on_top = True

    fieldsets = [
        (None, {'fields': ["name", "surname", "category", "is_active"]}),
        ('Прочие данные', {'fields': [],
                           'classes': ['collapse']}),
    ]


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu", "name", "slug", "parent", "parent", "published", "ordering"]

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)

admin.site.register(Snipet)
