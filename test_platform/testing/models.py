from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# importar modelo user
from django.contrib.auth.models import User
#importar modelo user, no definirlo aqui

# class User(User):

# Create Models Here

#user test crear realcionado con test 
class Test(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tests")
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    is_from_json = models.BooleanField(default=False)
    #soft skills relacion con tabla grupo montse
    #hard skills relacion con tabla grupo montse

class QuestionType(models.Model):
    code = models.CharField( max_length=50)
    name = models.CharField(max_lenght=50)
    def _str_(self):
        return self.nombre
    
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=200)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #relacionar la pregunta con la respuesta, hecho en json
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #relacion con user test, id respuesta usuario, id test 
    selected_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    #relacionar hard skills con user test

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

