from django.contrib import admin

from collection.models import Collection, CollectionImage


class CollectionImageInline(admin.TabularInline):
    model = CollectionImage


class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    inlines = [ CollectionImageInline, ]


admin.site.register(Collection, CollectionAdmin)