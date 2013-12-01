from django.db import models

class OwnerContact(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name=u'Email', max_length=50, blank=True, null=True)
    phone = models.CharField(verbose_name=u'Phone', max_length=50, blank=True, null=True)
    address = models.CharField(verbose_name=u'Address', max_length=50, blank=True, null=True)

    is_enabled = models.BooleanField(verbose_name=u'Enabled', default=False)

    def __unicode__(self):
        return (u"%s") % (self.name)


    def save(self):
        if self.is_enabled:
            try:
                temp = OwnerContact.objects.get(is_enabled=True)
                if self != temp:
                    temp.is_enabled = False
                    temp.save()
            except OwnerContact.DoesNotExist:
                pass
        super(OwnerContact, self).save()


    class Meta:
        verbose_name = (u"Owner Contact")
        verbose_name_plural = (u"Owner Contacts")
        ordering = ['-is_enabled']

