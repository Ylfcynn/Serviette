# test_models.py

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db    # pytestmark allows writing to the database.


class TestUser:
    """
    The first parameter in isinstance() is the string caster because str() calls the __str__ of an object.
    If the __str__ is faulty, returned value won't be a string.
    """
    def test_init(self):
        user = mixer.blend('accounts.User')
        assert user.pk == 1, 'This must save an instance but it didn\'t. Major fail. You lose.'

    def test_str_method(self):
        user = mixer.blend('accounts.User', name='1337 h4XX0r')    # Make a user, name it '1337 h4XX0r', check for the following attributes:
        assert str(user) != None, 'Fool! This must return something!'
        assert isinstance(str(user), str) == True, 'This must return string, dammit!'
        assert str(user) == '1337 h4XX0r', 'This must have a __str__ method. Another major fail. You suck.'