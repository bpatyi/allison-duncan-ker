from django.db import models
from autoslug import AutoSlugField

from section.models import Section

def image_fancy_path(instance, filename):
    return 'images/%s/' % self.instance.collection.slug



class Collection(models.Model):
    title = models.CharField(verbose_name=u'Collection title', max_length=50, blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(verbose_name=u'Collection description')
    section = models.ForeignKey(Section, verbose_name=u'Section')

    def __unicode__(self):
        return (u"%s") % (self.title)


    class Meta:
        verbose_name = u'Collection'
        verbose_name_plural = (u"Collections")
        ordering = ['title']


class CollectionImage(models.Model):
    collection = models.ForeignKey(Collection, verbose_name=u'Collection', blank=False, null=False)
    title = models.CharField(verbose_name=u'Image title', max_length=30, blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(verbose_name=u'Image description')
    image = models.ImageField(verbose_name='Image', upload_to=image_fancy_path)

    def __unicode__(self):
        return (u"%s") % (self.title)


    class Meta:
        verbose_name = u'Image'
        verbose_name_plural = (u"Images")
        ordering = ['title']
