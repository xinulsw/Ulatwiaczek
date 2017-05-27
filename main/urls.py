from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'test/$', views.test_lista, name='test_lista'),
    url(r'test/dodaj/$', views.test_dodaj, name='test_dodaj'),
    url(r'test/(?P<id>[0-9]+)/$', views.test_szczegoly, name='test_szczegoly'),
    url(r'test/(?P<id>[0-9]+)/usun/$', views.test_usun, name='test_usun'),
    url(r'test/(?P<id>[0-9]+)/edytuj/$', views.test_edytuj, name='test_edytuj'),

    url(r'sprawdzian/$', views.sprawdzian_lista, name='sprawdzian_lista'),
    url(r'sprawdzian/dodaj/$', views.sprawdzian_dodaj, name='sprawdzian_dodaj'),
    url(r'sprawdzian/(?P<id>[0-9]+)/$', views.sprawdzian_szczegoly, name='sprawdzian_szczegoly'),
    url(r'sprawdzian/(?P<id>[0-9]+)/usun/$', views.sprawdzian_usun, name='sprawdzian_usun'),
    url(r'sprawdzian/(?P<id>[0-9]+)/edytuj/$', views.sprawdzian_edytuj, name='sprawdzian_edytuj'),

    url(r'przedmiot/$', views.przedmiot_lista, name='przedmiot_lista'),
    url(r'przedmiot/dodaj/$', views.przedmiot_dodaj, name='przedmiot_dodaj'),

]
