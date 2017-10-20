from django.conf.urls import url

from .views import * 


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', VideoPerSubject, name='videolist'),
]
