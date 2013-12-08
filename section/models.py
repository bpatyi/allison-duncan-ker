from django.db import models
from autoslug import AutoSlugField


class Section(models.Model):
    order = models.IntegerField(verbose_name=u'Section order', unique=True)
    title = models.CharField(verbose_name=u'Section Title', max_length=30, blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(verbose_name=u'Section description')
    image = models.ImageField(verbose_name=u'Section promo image', upload_to='promo_images/', blank=True, null=True)

    def __unicode__(self):
        return (u"%s") % (self.title)


    class Meta:
        verbose_name = u'Section'
        verbose_name_plural = (u"Sections")
        ordering = ['order']
