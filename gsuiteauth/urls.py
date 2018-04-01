from django.conf.urls import url, include
from gsuiteauth import views as gsuite_views

urlpatterns = [
    url(r'^$', gsuite_views.index, name='index'),
    url(r'^test$', gsuite_views.test_api_request, name='test_api_request'),
    url(r'^authorize$', gsuite_views.authorize, name='authorize'),
    url(r'^oauth2callback$', gsuite_views.oauth2callback, name='oauth2callback'),
    url(r'^revoke$', gsuite_views.revoke, name='revoke'),
    url(r'^clear/$', gsuite_views.clear_credentials, name='clear_credentials'),
]