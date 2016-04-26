from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+)/$', views.ItemsView.as_view(), name='items'),
    url(r'^(?P<slug>[-\w\d]+).html', views.ItemView.as_view(), name='item'),
]
