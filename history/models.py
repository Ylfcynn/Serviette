from django.db import models
from accounts.models import User

# Create your models here.


class RoBit(models.Model):
    """
    This is an Ethereum 'smart contract' articulated as a automaton called a 'RoBit'. Multiple types will be selectable.

    """

    ROBIT_TYPES = (
        ('Timer', 'Timer switch'),
        ('Sensor', 'Sensor switch'),
    )

    name = models.CharField(max_length=256)
    type = models.CharField(max_length=12)
    description = models.CharField(max_length=2048)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    is_launched = models.BooleanField(default=False)
    launched_on = models.DateTimeField()
    trigger_date = models.DateTimeField()
    payload = models.CharField(max_length=20480)

    # Many to one. This is what necessitated the 'from django.contrib.auth.models import User' above.
    author = models.ForeignKey(User, related_name='robits')
    recipient_addresses = models.CharField(max_length=512)

    def __str__(self):
        """

        :return:
        """

        return self.name