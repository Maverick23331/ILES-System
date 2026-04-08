from rest_framework.permissions import BasePermission

class IsOwnerOfLog(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user

class IsAssignedSupervisor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student.workplace_supervisor.user == request.user
    
class CanViewLog(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        if user.role == 'student':
            return obj.student == user
        
        if user.role == 'workplace_supervisor':
            return obj.internship.workplace_supervisor.user == user

        if user.role == 'academic_supervisor':
            return obj.internship.academic_supervisor.user == user
        
        if user.role == 'admin':
            return True 
        return False
class CanCreateLog(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'
    
class CanEditLog(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user and obj.internship.workplace_supervisor.user == request.user