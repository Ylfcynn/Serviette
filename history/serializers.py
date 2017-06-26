from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class RoBitModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'type', 'description', 'created_on', 'modified_on',
                  'is_launched', 'launched_on', 'trigger_date', 'payload')
