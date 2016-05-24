"""affordability_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

import proto1.urls
import v2.urls
from affordability_model import google_auth

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^proto1/', include(proto1.urls)),
    url(r'^v2/', include(v2.urls)),
    url(r'^accounts/google/login', google_auth.login, name='google_login'),
    url(r'^accounts/google/oauth2', google_auth.oauth2, name='google_oauth2'),
    url(r'', RedirectView.as_view(permanent=False, pattern_name='proto1_home'))
]
