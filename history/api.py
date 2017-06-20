
from rest_framework import viewsets
from .models import RoBit
from .serializers import RoBitModelSerializer


# ViewSets define the view behavior.
class RoBitViewSet(viewsets.ModelViewSet):
    model = RoBit
    queryset = RoBit.objects.all()
    serializer_class = RoBitModelSerializer
