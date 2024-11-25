from django.db import models
from django.contrib.auth.hashers import make_password, check_password

#importar modelo user, no definirlo aqui

# Create Models Here

class User(models.Model):
    is_headhunter = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=128)  # Espacio suficiente para almacenar contraseñas cifradas

    def set_password(self, raw_password):
        """Configura la contraseña utilizando un hash seguro."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica si la contraseña ingresada coincide con la almacenada."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

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





class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()
    question_type = models.CharField(
        max_length=50, choices=[("MCQ", "Multiple Choice"), ("TF", "True/False")]
    )
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

