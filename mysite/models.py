from django.db import models
from django.contrib.sites.models import Site

Site.add_to_class('fb_page_url', models.URLField(max_length=200, verbose_name=u'Facebook page url', null=True, blank=True))
Site.add_to_class('page_title', models.CharField(max_length=50, verbose_name=u'Page title'))
Site.add_to_class('page_subtitle', models.CharField(max_length=50, verbose_name=u'Page subtitle', null=True, blank=True))
Site.add_to_class('billboard_image', models.ImageField(max_length=100, upload_to='billboard_images/', verbose_name=u'Billboard image', null=True, blank=True))



