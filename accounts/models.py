from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


class RoBit(models.Model):
    """
    This is an Ethereum 'smart contract' articulated as a automaton called a 'RoBit'. Multiple types will be selectable.

    """

    name = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)

    # Many to one. This is what necessitated the 'from django.contrib.auth.models import User' above.
    author = models.ForeignKey(User, related_name="robits")
    email_address = models.EmailField()

    def __str__(self):
        """

        :return:
        """

        return self.name



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


