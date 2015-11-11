from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from ietf.codematch import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^about/$', views.about, name="about"),
                       url(r'^back/$', views.back, name="back"),

                       # Accounts
                       url(r'^accounts/$', include('ietf.codematch.accounts.urls')),

                       # Matches
                       url(r'^matches/$', include('ietf.codematch.matches.urls')),

                       # Requests
                       url(r'^requests/$', include('ietf.codematch.requests.urls')),

                       )
