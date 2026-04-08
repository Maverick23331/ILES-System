from django.db import models
from django.conf import settings

class Intern(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    intern = models.OneToOneField(Intern, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.intern.name}'s Profile"
    
class StudentDocument(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    document =models.FileField(upload_to='intern_documents/')
    description = models.CharField(max_length=260, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    

    