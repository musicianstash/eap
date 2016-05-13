from eap.apps.catalog.models import Category


def predict_category_id_from_text(classifiers):
    return None


def get_category_from_category_name(category_name):
    return Category.objects.get(name__istartswith=category_name)
