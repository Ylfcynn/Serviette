# test_models.py

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db  # pytestmark allows writing to the database. "Please let us write to the database."


class TestRoBit:
    """
    The first parameter in isinstance() is the string caster because str() calls the __str__ of an object.
    If the __str__ is faulty, returned value won't be a string.
    """

    #
    def test_init(self):
        robit = mixer.blend('workspace.RoBit')
        assert robit.pk == 1, 'This must save an instance but it didn\'t. Major fail. You lose.'

    def test_str_method(self):
        robit = mixer.blend('workspace.RoBit', name='Roby_the_RoBit')    # Make a robit, name it 'Roby_the_RoBit', check for the following attributes:
        # assert + <bool>
        assert str(robit) != None, 'Fool! This must return something!'
        assert isinstance(str(robit), str) == True, 'This must return string, dammit!'
        assert str(robit) == 'Roby_the_RoBit', 'This must have a __str__ method. Another major fail. You suck.'