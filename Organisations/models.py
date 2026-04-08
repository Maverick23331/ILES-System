from django.db import models
from django.conf import settings

class Organisation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField()
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='departments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class InternSupervisor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name = 'supervisors')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='supervisors')
    position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)    
    phone_number = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.user.username


