from menu.models import MenuItem

def menu_processor(request):
    try:
        menus = MenuItem.objects.all()
    except MenuItem.DoesNotExist:
        menus = None

    context = {
        'menus': menus,
    }

    return context