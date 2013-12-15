from django.contrib import admin
from section.models import Section

from django.conf import settings


class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = ('order', 'title', 'image')

    class Media:
        if settings.HEROKU is True:
            js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'grappelli/tinymce_setup/tinymce_setup.js',)
        else:
            js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/grappelli/tinymce_setup/tinymce_setup.js',)


admin.site.register(Section, SectionAdmin)
