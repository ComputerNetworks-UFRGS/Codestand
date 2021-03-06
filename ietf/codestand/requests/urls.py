from django.conf.urls import url
from ietf.codestand.requests import views

urlpatterns = [
    url(r'^show_list/$', views.show_list, name="ietf.codestand.requests.views.show_list"),
    url(r'^show_list/(?P<type_list>.*)/(?P<att>.*)/(?P<state>.*)/(?P<page>.*)$', views.show_list,
        name="ietf.codestand.requests.views.show_list"),
    url(r'^show_list/(?P<type_list>.*)/(?P<att>.*)/(?P<state>.*)$', views.show_list,
        name="ietf.codestand.requests.views.show_list"),
    url(r'^show_list/(?P<type_list>.*)/(?P<att>.*)$', views.show_list, name="ietf.codestand.requests.views.show_list"),
    url(r'^show_list/(?P<type_list>.*)$', views.show_list, name="ietf.codestand.requests.views.show_list"),
    url(r'^new/$', views.new, name="ietf.codestand.requests.views.new"),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit, name="ietf.codestand.requests.views.edit"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="ietf.codestand.requests.views.delete"),
    url(r'^delete/(?P<pk>[0-9]+)/(?P<template>.+)$', views.delete, name="ietf.codestand.requests.views.delete"),
    url(r'^archive/(?P<pk>[0-9]+)$', views.archive, name="ietf.codestand.requests.views.archive"),
    url(r'^remove_contact/(?P<pk>[0-9]+)/(?P<contact_name>.+)$', views.remove_contact,
        name="ietf.codestand.requests.views.remove_contact"),
    url(r'^remove_document/(?P<pk>[0-9]+)/(?P<doc_name>.+)$', views.remove_document,
        name="ietf.codestand.requests.views.remove_document"),
    url(r'^remove_tag/(?P<pk>[0-9]+)/(?P<tag_name>.+)$', views.remove_tag, name="ietf.codestand.requests.views.remove_tag"),
    url(r'^search/$', views.search, name="ietf.codestand.requests.views.search"),
    url(r'^search/(?P<type_list>.*)$', views.search, name="ietf.codestand.requests.views.search"),
    url(r'^(?P<pk>[0-9]+)/$', views.show, name="ietf.codestand.requests.views.show"),
]
