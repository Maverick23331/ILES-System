from django.contrib import admin
from .models import Internship, InternshipApplication, InternshipLocation, internshipSchedule

admin.site.register(Internship)
admin.site.register(InternshipApplication)
admin.site.register(InternshipLocation)     
admin.site.register(internshipSchedule)
# Register your models here.
