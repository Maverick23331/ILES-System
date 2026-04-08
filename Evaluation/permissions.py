from rest_framework.permissions import BasePermission

class CanEvaluateLog(BasePermission):
    def has_object_permission(self, request, view):
        return request.user.role == 'workplace_supervisor'
    
class IsAssignedSupervisor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.internship.workplace_supervisor.user == request.user
    
class IsEvaluationOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.WorkplaceSupervisor.user == request.user
    
class CanViewEvaluation(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        if user.role == 'workplace_supervisor':
            return obj.internship.workplace_supervisor.user == user

        if user.role == 'academic_supervisor':
            return obj.internship.academic_supervisor.user == user
        
        if user.role == 'admin':
            return True 
        return False

    
    