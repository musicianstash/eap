from eap.apps.catalog.models import Category
from eap.apps.home.models import Slider


def item_categories(request):
    categories = Category.objects.root_nodes()
    return {
        'item_categories': categories
    }


def popular_categories(request):
    categories = Category.objects.filter(is_popular=True).all()
    return {
        'popular_categories': categories
    }


def home_slides(request):
    return {
        'home_slides': Slider.objects.all()
    }
