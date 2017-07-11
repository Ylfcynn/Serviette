"""
test_forms.py
"""

from workspace import forms


class TestCreateRoBitForm:
    """

    """
    def test_form(self):
        form = forms.CreateRoBitForm(data={})
        assert form.is_valid() is False, 'No data you douchebag! This *must* be invalid!'

        data = {'robit_name': ''}
        form = forms.CreateRoBitForm(data=data)
        assert form.is_valid() is False, 'There\'s no RoBit name dummy! This *must* be invalid!'
        assert 'robit_name' in forms.errors, 'A field error *must* be returned for \'RoBit name\' you ass!'

        data = {'robit_name': 'Roby'}
        form = forms.CreateRoBitForm(data=data)
        assert form.is_valid() is True, 'The RoBit has a name. It\'s valid, fool!'