from rest_framework.viewsets import ModelViewSet
from .models import Organisation
from .serializers import OrganisationSerializer

class OrganisationViewSet(ModelViewSet):
    query_set = Organisation.objects.all()
    serializer_class = OrganisationSerializer

# Create your views here.
