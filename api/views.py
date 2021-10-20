from rest_framework import viewsets

from api.serializers import PartnerSerializer
from web.models import Partner


class PartnerViewSet(viewsets.ModelViewSet):
    """
    Methods: GET, POST, PUT, DELETE
    URL_PATH: /api/partners/

    TODO: Custom Response
    """
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
