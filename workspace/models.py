from django.db import models
from accounts.models import User

# Create your models here.


class RoBit(models.Model):
    """
    This is an Ethereum 'smart contract' articulated as a automaton called a 'RoBit'. Multiple types will be selectable.

    """
    # A feature down the road.
    # ROBIT_TYPES = (
    #     ('Timer', 'Timer switch'),
    #     ('Sensor', 'Sensor switch'),
    # )

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    is_launched = models.BooleanField(default=False)
    launched_on = models.DateTimeField()
    solidity_code = models.CharField(max_length=20480)

    # Many to one. This is what necessitated the 'from django.contrib.auth.models import User' above.
    author = models.ForeignKey(User, related_name='robits')

    def __str__(self):
        """

        :return:
        """

        return self.name
