"""Serviette URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.api import UserViewSet
from rest_framework import routers
from history.api import RoBitViewSet


# TODO: Make this part work
from pages.views import index

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'RoBit', RoBitViewSet)

urlpatterns = [
    # The kwargs below are for self documentation & reverse URL resolution (e.g. menus).
    url(r'^admin/', admin.site.urls, name='admin'),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),    # Indicating API version is a common convention

    url(r'^/', index, name='index'),
    # url(r'^about/', about, name='about'),
    # url(r'^contact/', contact, name='contact'),
    # url(r'^login/', login, name='login'),
    # url(r'^my_account/', my_account, name='my_account'),
    # url(r'^new_account/', new_account, name='new_account'),
    # url(r'^workspace/', workspace, name='workspace'),
    # url(r'^workspace/create/', create, name='create'),
    # url(r'^workspace/delete/', delete, name='delete'),
    # url(r'^workspace/edit/', edit, name='edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)