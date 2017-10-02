# -*- coding: utf-8 -*-

from bdpy3_web_app import views
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()


urlpatterns = [

    url( r'^admin/', admin.site.urls ),  # eg host/project_x/admin/

    url( r'^info/$', views.info, name='info_url' ),

    ]
