from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class RoBitModelSerializer(serializers.HyperlinkedModelSerializer.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'type', 'description', 'created_on', 'modified_on', 'is_launched', 'launched_on',)

        #  = models.CharField(max_length=256)
        # type = models.CharField(max_length=12)
        # description = models.CharField(max_length=2048)
        # created_on = models.DateTimeField(auto_now_add=True)
        # modified_on = models.DateTimeField(auto_now_add=True)
        # is_launched = models.BooleanField(default=False)
        # launched_on = models.DateTimeField()
        # trigger_date = models.DateTimeField()
        # payload =