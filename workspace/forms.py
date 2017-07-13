from .models import RoBit
from django import forms


solidity_example = """
/* The Greeter is an intelligent digital entity that lives on the blockchain and is able 
to have conversations with anyone who interacts with it, based on its input.*/
contract mortal {
    // Define variable owner of the type address
    address owner;

    // This function is executed at initialization and sets the owner of the contract
    function mortal() { owner = msg.sender; }

    // Function to recover the funds on the contract
    function kill() { if (msg.sender == owner) selfdestruct(owner); }
}

contract greeter is mortal {
    // Defines variable greeting of the type string
    string greeting;

    // This runs when the contract is executed
    function greeter(string _greeting) public {
        greeting = _greeting;
    }

    // Main function
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
