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

    email = models.EmailField()

    REQUIRED_FIELDS = ['email']


    # def __str__(self):
    #     """
    #
    #     :return:
    #     """
    #
    #     return self.name



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


