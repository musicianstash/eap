from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ArticlesListView.as_view(), name='articles'),
    url(r'^(?P<slug>[-\w\d]+).html', views.ArticleView.as_view(), name='article'),
]
