from django.contrib import admin

from site_owner_contact.models import OwnerContact


class OwnerContactAdmin(admin.ModelAdmin):
    model = OwnerContact
    list_display = ('name', 'email', 'phone', 'address', 'is_enabled')


admin.site.register(OwnerContact, OwnerContactAdmin)
