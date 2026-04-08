from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .models import Student

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'student':
            Student.objects.create(user=instance)
            
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 'student':
        instance.student.save()
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'student':
        print(f"Creating student profile for user: {instance.username}")