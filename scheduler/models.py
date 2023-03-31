from django.db import models

# Create your models here.
class InbodyImage(models.Model):
    image= models.ImageField(upload_to="image")

class ChatGPTResponse(models.Model):
    response= models.TextField()
