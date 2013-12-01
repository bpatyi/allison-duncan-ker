from django.db import models
from autoslug import AutoSlugField

from django.contrib.flatpages.models import FlatPage
from section.models import Section


class MenuItem(models.Model):
    order = models.IntegerField(verbose_name=u'Order', null=False, blank=False, unique=True)
    title = models.CharField(verbose_name=u'Menu Title', null=False, blank=False, max_length=50)
    slug = AutoSlugField(populate_from='title')
    flatpage = models.ForeignKey(FlatPage, verbose_name=u'Flatpage', blank=True, null=True)
    url = models.CharField(verbose_name=u'Url', blank=True, null=True, max_length=50, help_text=u'like /about/')
    section = models.ForeignKey(Section, verbose_name=u'Section', blank=True, null=True)


    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.flatpage:
            return self.flatpage.url


    def __unicode__(self):
        return (u"%s") % (self.title)


    class Meta:
        verbose_name = u'Menu Item'
        verbose_name_plural = (u"Menu Items")
        ordering = ['order']