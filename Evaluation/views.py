from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Evaluation
from .serializers import EvaluationSerializer
from .permissions import (
    CanEvaluateLog,
    IsAssignedSupervisor,
    IsEvaluationOwner,
    CanViewEvaluation
)

class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_clases = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
    
        if user.role == 'student':
            return Evaluation.objects.filter(internship__student=user)
        
        if user.role == 'workplace_supervisor':
            return Evaluation.objects.filter(internship__workplace_supervisor__user=user)   
        
        if user.role == 'academic_supervisor':
            return Evaluation.objects.filter(internship__academic_supervisor__user=user)    
        
        if user.role == 'admin':
            return Evaluation.objects.all() 
        
        return Evaluation.objects.none()
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), CanEvaluateLog()]
        
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAssignedSupervisor()]
        
        elif self.action == 'retrieve':
            return [IsAuthenticated(), CanViewEvaluation()]   
          
        elif self.action == 'list':
            return [IsAuthenticated()]
        
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        user = self.request.user
        worklog = serializer.validated_data['worklog']
        
        if worklog.student.workplace_supervisor != user:
            raise ValidationError("You are not assigned to this student's internship.")
        
        if Evaluation.objects.filter(worklog=worklog).exists():
            raise ValidationError("This work log has already been evaluated.")
        
        serializer.save(workplace_supervisor=user)
            
    
    

# Create your views here.
 