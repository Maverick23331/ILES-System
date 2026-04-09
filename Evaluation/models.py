from django.db import models
from django.conf import settings

class Evaluation(models.Model):
    internship = models.ForeignKey('Internships.Internship', on_delete=models.CASCADE, related_name='evaluations')
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE, related_name='evaluations')
    supervisor = models.ForeignKey('Organisations.InternSupervisor', on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField()
    evaluated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Evaluation for {self.student}" 

class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name
    
class EvaluationScore(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='scores')
    criteria = models.ForeignKey(EvaluationCriteria, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    
    def calculate_total_score(self):
        total_score = sum(score.score for score in self.evaluation.scores.all())
        scores = self.evaluation.scores.all()
        return total_score / scores.count() if scores.exists() else 0

    def __str__(self):
        return f"{self.criteria} - {self.score}"
    
class FinalEvaluation(models.Model):
    internship = models.ForeignKey('Internships.Internship', on_delete=models.CASCADE, related_name='final_evaluations')
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE, related_name='final_evaluations')
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='final_evaluation', null=True, blank=True)
    supervisor = models.ForeignKey('Organisations.InternSupervisor', on_delete=models.CASCADE, related_name='final_evaluations')
    final_score = models.DecimalField(max_digits=5, decimal_places=2)
    evaluated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Final Evaluation for {self.student}"
    
class SupervisorFeedback(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='supervisor_feedback')
    supervisor = models.ForeignKey('Organisations.InternSupervisor', on_delete=models.CASCADE)   
    feedback = models.TextField()
    strengths = models.TextField()
    weaknesses = models.TextField()
    suggestions = models.TextField()
    recommendation = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
