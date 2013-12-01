from django.contrib import admin

from menu.models import MenuItem
from menu.forms import MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    form = MenuItemForm
    list_display = ('order', 'title', 'flatpage', 'url', 'section')


admin.site.register(MenuItem, MenuItemAdmin)