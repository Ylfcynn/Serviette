"""
test_views.py
"""

import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from accounts.views import profile
from accounts.models import User


class TestAdminView:
    """

    """
    def test_anonymous(self):
        """

        :return:
        """
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = profile(request)
        assert 'login' in response.url, 'Anonymous users must login to view their profile page, dummy.'

    def test_superuser(self):
        """

        :return:
        """
        user = mixer.blend(User, is_superuser=True)
        request = RequestFactory().get('/')
        request.user = user
        response = profile(request)
        assert response.status_code == 200, 'Must be viewable as a superuser. You screwed up!'
