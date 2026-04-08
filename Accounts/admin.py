from django.contrib import admin
from .models import User, Student, Organization, WorkplaceSupervisor, AcademicSupervisor  

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Organization)
admin.site.register(WorkplaceSupervisor)
admin.site.register(AcademicSupervisor)
