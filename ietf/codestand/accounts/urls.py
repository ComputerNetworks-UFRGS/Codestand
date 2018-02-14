from django.conf.urls import url
from django.contrib.auth.views import login, logout
from ietf.codestand.accounts import views

urlpatterns = [
    url(r'^$', views.index, name='ietf.codestand.accounts.views.index'),
    url(r'^login/$', login, {'template_name': 'codestand/accounts/login.html'}, name='django.contrib.auth.views.login'),
    url(r'^logout/$', logout, {'template_name': 'codestand/index.html'}, name='django.contrib.auth.views.logout'),
    url(r'^register/$', views.register, name='ietf.codestand.accounts.views.register'),
    url(r'^profile/$', views.profile, name='ietf.codestand.accounts.views.profile'),
    url(r'^profile/(?P<user>[0-9]+)/$', views.profile, name='ietf.codestand.accounts.views.profile'),
    url(r'^top_coders/$', views.top_coders, name='ietf.codestand.accounts.views.top_coders'),
    url(r'^statistics/([0-9]+)/$', views.statistics, name='ietf.codestand.accounts.views.statistics'),
]
