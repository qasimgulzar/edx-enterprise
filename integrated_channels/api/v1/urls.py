# -*- coding: utf-8 -*-
"""
URL definitions for v1 Integrated Channel API endpoints.
"""

from django.conf.urls import include, url

app_name = 'v1'
urlpatterns = [
    url(r'^moodle/', include('integrated_channels.api.v1.moodle.urls')),
]
