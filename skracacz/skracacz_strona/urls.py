from django.conf.urls import include, url
from skracacz_strona.views import index, redirect_original,shorten_url
 
urlpatterns = [
    url(r'^$', index, name='home'),
 
    url(r'^(?P<short_id>\w{6})$', redirect_original, name='redirectoriginal'),
 
    url(r'^makeshort/$', shorten_url, name='shortenurl'),

]