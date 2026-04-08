from django.db import models
from django.conf import settings

class WorkLog(models.Model):
    internship = models.ForeignKey('Internships.Internship', on_delete=models.CASCADE, related_name='work_logs')
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE, related_name='work_logs')
    title = models.CharField(max_length=255)
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    approved = models.BooleanField(default=False)   
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    supervisor_comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student} - {self.internship} - {self.date}"
    
class WorkLogAttachment(models.Model):
    work_log = models.ForeignKey(WorkLog, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='work_log_attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class WorkLogComment(models.Model):
    work_log = models.ForeignKey(WorkLog, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    
class WeeklySummary(models.Model):
    internship = models.ForeignKey('Internships.Internship', on_delete=models.CASCADE, related_name='weekly_summaries')
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE, related_name='weekly_summaries')
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student} - {self.internship} - {self.week_start_date} to {self.week_end_date}"
    
class WorklogEvaluation(models.Model):
    work_log = models.ForeignKey(WorkLog, on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField()
    evaluated_at = models.DateTimeField(auto_now_add=True)
    

    
    