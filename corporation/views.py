from rest_framework.viewsets import ModelViewSet

from .models import Corporation
from .serializers import CorporationSerializer


class CorporationViewSetsAPIView(ModelViewSet):
    """this viewset enables the full crud which are create, retrieve,update and delete  """
    serializer_class = CorporationSerializer
    queryset = Corporation.objects.all()
