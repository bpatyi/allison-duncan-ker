from django.contrib import admin

from section.models import Section


class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = ('order', 'title', 'image')


admin.site.register(Section, SectionAdmin)
