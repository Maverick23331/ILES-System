from rest_framework.viewsets import ModelViewSet
from .models import Internship
from .serializers import InternshipSerializer

class InternshipViewSet(ModelViewSet):
    query_set = Internship.objects.all()
    serializer_class = InternshipSerializer
    
# Create your views here.
