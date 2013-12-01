from site_owner_contact.models import OwnerContact
from django.conf import settings


def contact_processor(request):
    try:
        contact = OwnerContact.objects.get(is_enabled=True)
    except OwnerContact.DoesNotExist:
        contact = None

    context = {
        'contact': contact,
    }

    return context