from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# Create your models here.


class User(AbstractUser):
    """
    Users with the Django authentication system are represented by this model.
    These are my users. There are many like them but these are my own.
    User name and password are required.

    """

    ORBIT_TYPES = (
        ('atomic', 'Electron shell schema'),      # K: 2, L: 8, M: 18, N: 32, O: 50, P: 72
        ('planetary', 'Solar system schema'),   # One RoBit per orbit radius
        # ('dyson', 'Dyson sphere schema'),       # Tiling arrangement in the form of a shell
    )

    email = models.EmailField()
    orbit_schema = models.CharField(max_length=128, choices=ORBIT_TYPES)

    REQUIRED_FIELDS = ['email']


    def __str__(self):
        """

        :return:
        """

        return self.username



# class Llamas(): # Slugfield class
#     """
#     Auto sets the slug field as the name field on save.
#     """
#     name = models.CharField(max_length=256)
#     slug = models.SlugField(editable=False, blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#             self.slug = slugify(self.name)
#
#          super().save(*args, **kwargs)


