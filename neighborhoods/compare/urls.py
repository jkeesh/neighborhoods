from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^compare/(?P<city1>\w+)/(?P<city2>\w+)$', views.compare, name='compare'),

    url(r'^view/(?P<city1>\w+)/(?P<city2>\w+)$', views.view, name='view'),

    url(r'^save_results$', views.save, name='save'),

]
