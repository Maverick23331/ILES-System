from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'    
    
class Iswork_Supervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'work_supervisor'
    
class IsAcademic_Supervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'academic_supervisor'
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' 
    
