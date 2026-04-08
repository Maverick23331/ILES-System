from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = [
    ('student', 'Student'),
    ('workplace_supervisor', 'Workplace Supervisor'),
    ('academic_supervisor', 'Academic Supervisor'),
    ('admin', 'Admin'),
]
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled')
]

class User(AbstractUser):
    pass

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    year_of_study = models.IntegerField()

    def __str__(self):
        return self.user.username

class Organization(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class WorkplaceSupervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    
class AcademicSupervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    
class Internship(models.Model):
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE)
    organization = models.ForeignKey('Accounts.Organization', on_delete=models.CASCADE)
    workplace_supervisor = models.ForeignKey('Accounts.WorkplaceSupervisor', on_delete=models.CASCADE)
    academic_supervisor = models.ForeignKey('Accounts.AcademicSupervisor', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='pending')
    
class WorkLog(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    hours_worked = models.FloatField()
    approved = models.BooleanField(default=False)
    
class Evaluation(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    evaluation = models.ForeignKey('Accounts.WorkLog', on_delete=models.CASCADE)
    score = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
