from rest_framework import viewsets, permissions
from leads.models import Lead
from .serializers import LeadSerializer

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    quaryset = Lead.objects.all()
    permission_classes = [
        # permissions_AllowAny
    ]
    serializer_class = LeadSerializer
