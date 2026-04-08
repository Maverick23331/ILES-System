from django.contrib import admin
from .models import WorkLog, WorkLogAttachment, WorkLogComment, WeeklySummary, WorklogEvaluation
admin.site.register(WorkLog)
admin.site.register(WorkLogAttachment)      
admin.site.register(WorkLogComment)
admin.site.register(WeeklySummary)
admin.site.register(WorklogEvaluation)

# Register your models here.

