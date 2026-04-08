from rest_framework.viewsets import ModelViewSet
from .models import Intern
from .serializers import InternSerializer

class InternViewSet(ModelViewSet):
    query_set = Intern.objects.all()
    serializer_class = InternSerializer
# Create your views here.
