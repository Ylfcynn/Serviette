"""
Serviette URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from accounts.api import UserViewSet
from pages.views import about, contact, help, handler404, handler500
# TODO: Make this part work
from pages.views import index
from workspace.api import RoBitViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'RoBit', RoBitViewSet)

urlpatterns = [
    # The kwargs below are for self documentation & reverse URL resolution (e.g. menus).

    # Admin and Honeypot  TODO: Honeypot
    url(r'^admin/', admin.site.urls, name='admin'),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API

    # API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),    # Indicating API version is a common convention

    # Pages
    url(r'^$', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'^help/', help, name='help'),
    url(r'^sitemap/', help, name='sitemap'),
    url(r'^terms/', help, name='terms'),
    url(r'^404/', handler404, name='handler404'),
    url(r'^500/', handler500, name='handler500'),

    # Accounts
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # Workspace
    url(r'^workspace/', include('workspace.urls', namespace='workspace')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
