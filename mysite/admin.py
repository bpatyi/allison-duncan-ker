from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin


SiteAdmin.list_display += ('fb_page_url', 'page_title', 'page_subtitle', 'billboard_image',)

