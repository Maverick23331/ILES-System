from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import WorkLog
from .serializers import WorkLogSerializer
from .permissions import (
    IsAssignedSupervisor,
    CanViewLog,
    CanCreateLog,
    CanEditLog
)

class WorkLogViewSet(ModelViewSet):
    queryset = WorkLog.objects.all()
    serializer_class = WorkLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        if user.role == 'student':
            return WorkLog.objects.filter(student=user) 
        
        if user.role == 'workplace_supervisor':
            return WorkLog.objects.filter(internship__workplace_supervisor__user=user)  

        if user.role == 'academic_supervisor':
            return WorkLog.objects.filter(internship__academic_supervisor__user=user)       
        
        if user.role == 'admin':
            return WorkLog.objects.all()            
        return WorkLog.objects.none()

    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), CanCreateLog()]
        
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), CanEditLog()]
        
        elif self.action == 'retrieve':
            return [IsAuthenticated(), CanViewLog()]   
          
        elif self.action == 'list':
            return [IsAuthenticated()]
        
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
        
    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        
        if user.role == 'student' and obj.student != user:
            raise PermissionDenied("You do not have permission to access this work log.")
        
        if user.role == 'workplace_supervisor' and obj.internship.workplace_supervisor.user != user:
            raise PermissionDenied("You do not have permission to access this work log.")
        
        if user.role == 'academic_supervisor' and obj.internship.academic_supervisor.user != user:
            raise PermissionDenied("You do not have permission to access this work log.")
        
        return obj
    
    def perform_update(self, serializer):
        obj = self.get_object()
        user = self.request.user
        
        if obj.student != user:
            raise PermissionDenied("You do not have permission to edit this work log.")
        
        if obj.internship.workplace_supervisor.user != user:
            raise PermissionDenied("You do not have permission to edit this work log.")
        
        serializer.save()