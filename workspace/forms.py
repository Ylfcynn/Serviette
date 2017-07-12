from .models import RoBit
from django import forms


solidity_example = """
contract mortal {
    /* Define variable owner of the type address*/
    address owner;

    /* this function is executed at initialization and sets the owner of the contract */
    function mortal() { owner = msg.sender; }

    /* Function to recover the funds on the contract */
    function kill() { if (msg.sender == owner) selfdestruct(owner); }
}

contract greeter is mortal {
    /* define variable greeting of the type string */
    string greeting;

    /* this runs when the contract is executed */
    function greeter(string _greeting) public {
        greeting = _greeting;
    }

    /* main function */
    function greet() constant returns (string) {
        return greeting;
    }
}
"""

class CreateRoBitForm(forms.ModelForm):

    class Meta:
        model = RoBit
        fields = ('name', 'type', 'description', 'solidity_code',)
        widgets = {'solidity_code': forms.Textarea(attrs={'class': 'solidity', 'placeholder': solidity_example})}


    # def clean_solidity_code(self):
    #     """
    #
    #     :return:
    #     """



class EditRoBitForm(forms.ModelForm):

    class Meta:
        model = RoBit
        fields = ('name', 'type', 'description', 'solidity_code',)
