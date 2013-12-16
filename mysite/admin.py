from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin
from django.conf import settings
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm

class MyFlatPageAdmin(FlatPageAdmin):

    class Media:
        if settings.HEROKU is True:
            js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'grappelli/tinymce_setup/tinymce_setup.js',)
        else:
            js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/grappelli/tinymce_setup/tinymce_setup.js',)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)

SiteAdmin.list_display += ('fb_page_url', 'page_title', 'page_subtitle', 'billboard_image',)

