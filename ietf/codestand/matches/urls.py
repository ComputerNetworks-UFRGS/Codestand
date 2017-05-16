from django.conf.urls import url
from ietf.codestand.matches import views

urlpatterns = [
    url(r'^show_list/$', views.show_list, name="ietf.codestand.matches.views.show_list"),
    url(r'^show_list/(?P<is_my_list>.*)/(?P<att>.*)/(?P<state>.*)/(?P<page>.*)$', views.show_list,
        name="ietf.codestand.matches.views.show_list"),
    url(r'^show_list/(?P<is_my_list>.*)/(?P<att>.*)/(?P<state>.*)$', views.show_list,
        name="ietf.codestand.matches.views.show_list"),
    url(r'^show_list/(?P<is_my_list>.*)/(?P<att>.*)$', views.show_list, name="ietf.codestand.matches.views.show_list"),
    url(r'^show_list/(?P<is_my_list>.*)$', views.show_list, name="ietf.codestand.matches.views.show_list"),
    url(r'^new/$', views.new, name="ietf.codestand.matches.views.new"),
    url(r'^new/(?P<pk>.*)/$', views.new, name="ietf.codestand.matches.views.new"),
    url(r'^edit/(?P<pk>[0-9]+)/(?P<ck>[0-9]+)$', views.edit, name="ietf.codestand.matches.views.edit"),
    url(r'^delete/(?P<pk>[0-9]+)/(?P<ck>[0-9]+)/(?P<template>.+)$', views.delete, name="ietf.codestand.matches.views.delete"),
    url(r'^delete/(?P<pk>[0-9]+)/(?P<ck>[0-9]+)$', views.delete, name="ietf.codestand.matches.views.delete"),
    url(r'^archive/(?P<ck>[0-9]+)/$', views.archive, name="ietf.codestand.matches.views.archive"),
    url(r'^remove_contact/(?P<ck>[0-9]+)/(?P<contact_name>.+)$', views.remove_contact,
        name="ietf.codestand.matches.views.remove_contact"),
    url(r'^remove_link/(?P<ck>[0-9]+)/(?P<link_name>.+)$', views.remove_link, name="ietf.codestand.matches.views.remove_link"),
    url(r'^remove_tag/(?P<ck>[0-9]+)/(?P<tag_name>.+)$', views.remove_tag, name="ietf.codestand.matches.views.remove_tag"),
    url(r'^remove_document/(?P<pk>[0-9]+)/(?P<doc_name>.+)$', views.remove_document,
        name="ietf.codestand.matches.views.remove_document"),
    url(r'^search/$', views.search, name="ietf.codestand.matches.views.search"),
    url(r'^search/(?P<is_my_list>.*)$', views.search, name="ietf.codestand.matches.views.search"),
    url(r'^(?P<pk>[0-9]+)/(?P<ck>[0-9]+)$', views.show, name="ietf.codestand.matches.views.show"),
]
