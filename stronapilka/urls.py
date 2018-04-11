from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<zawodnik_id>[0-9]+)/$', views.detail, name='detail'),
    	url(r'^(?P<zawodnik_id>[0-9]+)/results/$', views.results, name='results'),
	url('<int:zawodnik_id>/vote/', views.vote, name='vote'),
]
