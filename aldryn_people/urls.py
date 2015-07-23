# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from aldryn_people.views import GroupView, PersonView, DownloadVcardView

urlpatterns = patterns('',
    url(r'^group/(?P<pk>[0-9]+)/$',
        GroupView.as_view(), name='group-detail'),
    url(r'^group/(?P<slug>[A-Za-z0-9_\-]+)/$',
        GroupView.as_view(), name='group-detail'),

    url(r'^(?P<pk>[0-9]+)/$',
        PersonView.as_view(), name='person-detail'),
    url(r'^(?P<slug>[A-Za-z0-9_\-]+)/$',
        PersonView.as_view(), name='person-detail'),

    url(r'^(?P<pk>[0-9]+)/download/$',
        DownloadVcardView.as_view(), name='download_vcard'),
    url(r'^(?P<slug>[A-Za-z0-9_\-]+)/download/$',
        DownloadVcardView.as_view(), name='download_vcard'),
)
