from django.contrib import admin
from .models import Evaluation, EvaluationCriteria, EvaluationScore, FinalEvaluation, SupervisorFeedback
admin.site.register(Evaluation)     
admin.site.register(EvaluationCriteria)
admin.site.register(EvaluationScore)
admin.site.register(FinalEvaluation)
admin.site.register(SupervisorFeedback)

# Register your models here.
