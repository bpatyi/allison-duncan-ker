from django.contrib import admin

from filemanager.models import File

class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('pk', 'the_file', 'description')

admin.site.register(File, FileAdmin)
