from django.db import models
from django.conf import settings

class Internship(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organisation = models.ForeignKey('Organisations.Organisation', on_delete=models.CASCADE, related_name='internships')
    department = models.ForeignKey('Organisations.Department', on_delete=models.CASCADE, related_name='internships')
    supervisor = models.ForeignKey('Organisations.InternSupervisor', on_delete=models.CASCADE, related_name='internships')
    start_date = models.DateField()     
    end_date = models.DateField()
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student} - {self.organisation}"
    
class InternshipApplication(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='applications')
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Internship.STATUS_CHOICES, default='pending')
    
class InternshipLocation(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='locations')
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
class internshipSchedule(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    

# Create your models here.

