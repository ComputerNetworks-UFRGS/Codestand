from django.conf.urls import url, include
from ietf.codestand import views

urlpatterns = [
    url(r'^$', views.index, name='ietf.codestand.views.index'),
    url(r'^search/$', views.search, name="ietf.codestand.views.search"),
    url(r'^about/$', views.about, name="ietf.codestand.views.about"),  
    url(r'^back/$', views.back, name="ietf.codestand.views.back"),
    url(r'^sync/$', views.sync, name="ietf.codestand.views.sync"),
    # url(r'^dashboard/$', views.dashboard, name="dashboard"),
    # Accounts
    url(r'^accounts/', include('ietf.codestand.accounts.urls')),

    # Matches
    url(r'^matches/', include('ietf.codestand.matches.urls')),

    # Requests
    url(r'^requests/', include('ietf.codestand.requests.urls')),
 
]
