from django.db import models
from account.models import User

# Create your models here.
class InbodyImage(models.Model):
    image= models.ImageField(upload_to="image")

class ExerciseResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response= models.TextField()

class MealResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response= models.TextField()
