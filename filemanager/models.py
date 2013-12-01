from django.db import models

class File(models.Model):
    the_file = models.FileField(verbose_name=u'File', upload_to='files/%Y/%m/%d', blank=False, null=False)
    description = models.TextField(verbose_name=u'File description', blank=True, null=True)

    def __unicode__(self):
        return (u"%s") % (self.the_file)


    class Meta:
        verbose_name = u'File'
        verbose_name_plural = (u"Files")