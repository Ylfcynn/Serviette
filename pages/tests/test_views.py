"""
test_views.py
"""


from django.test import RequestFactory

from pages.views import index


class TestHomepageView:
    """

    """
    def test_index(self):
        request = RequestFactory().get('/')
        response = index(request)
        assert response.status_code == 200, 'Must be peachy keen. Hunky dory is not grasped dufus.'


