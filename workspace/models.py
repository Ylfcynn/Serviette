from django.db import models
from accounts.models import User
from datetime import datetime
from .schemata import SCHEMATA

# Create your models here.


class RoBit(models.Model):
    """
    This is an Ethereum 'smart contract' articulated as a automaton called a 'RoBit'. Multiple types are selectable.

    """
    ROBIT_TYPES = (
        ('Doohickey', 'Delightful doohickey'),
        ('Thingamajig', 'Thrilling thingamajig'),
    )

    name = models.CharField(max_length=256)
    type = models.CharField(max_length=24, choices=ROBIT_TYPES)
    description = models.CharField(max_length=2048)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    is_launched = models.BooleanField(default=False)
    launched_on = models.DateTimeField(blank=True, null=True)
    solidity_code = models.TextField(max_length=20480)

    # Many to one. This is what necessitated the 'from django.contrib.auth.models import User' above.
    author = models.ForeignKey(User, related_name='robits')

    class Meta:
        verbose_name = "RoBit"            # Overrides the 'humanizer' so that /admin shows the desired class name
        verbose_name_plural = "RoBits"



    def __str__(self):
        """

        :return:
        """

        return f'{self.name} | {self.type} | {self.is_launched}'

    def launch(self):
        """

        :return:
        """
        self.is_launched = True
        self.launched_on = datetime.now()

    def save(self, *args, **kwargs):
        """

        :return:
        """
        super().save(*args, **kwargs)


class Orbit(models.Model):
    """
    Defines the orbit of a RoBit in an A-Frame scene
    """

    robit = models.OneToOneField(RoBit)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    z = models.FloatField(default=0)

    def __str__(self):
        return f'{self.robit.name} | ({self.x}, {self.y}, {self.z})'


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        instance = Orbit(x=x, y=y, z=z)

        return instance

    def scenographer(self):
        """
        This is potentially confusing.
        count() returns an integer starting at 1 but access-by-index returns an integer starting at 0.
        A delta of 1 results, which is equivalent to an increment of 1. So, no '+1'.
        :return:
        """
        # import pdb; pdb.set_trace()
        schema = SCHEMATA[self.robit.author.orbit_schema]

        robbery_of_robits = self.robit.author.robits.all().count()
        self.x, self.y, self.z = schema[robbery_of_robits]

        return

    def save(self, *args, **kwargs):
        """

        :return:
        """
        self.scenographer()
        super().save(*args, **kwargs)