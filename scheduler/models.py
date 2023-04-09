from django.db import models
from account.models import User
# Create your models here.
class InbodyImage(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    image= models.ImageField(upload_to="image")
    inbody_score= models.CharField(max_length=30, null=True, blank=True)
    waist_hip_ratio= models.CharField(max_length=30, null=True, blank=True)

class ExerciseResponse(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    response= models.TextField()

class MealResponse(models.Model):
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    response= models.TextField()

class MetaData(models.Model):
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    state = models.TextField()
    purpose = models.TextField()
    place = models.TextField()
    body_component = models.TextField()
    routine = models.TextField()
    time = models.TextField()
