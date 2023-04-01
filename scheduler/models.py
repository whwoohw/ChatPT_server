from django.db import models

# Create your models here.
class InbodyImage(models.Model):
    image= models.ImageField(upload_to="image")

class ExerciseResponse(models.Model):
    response= models.TextField()

class MealResponse(models.Model):
    response= models.TextField()