from django.conf.urls import patterns, include, url

from core.views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
)