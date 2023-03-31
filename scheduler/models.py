from django.db import models

# Create your models here.
class InbodyImage(models.Model):
    image= models.ImageField(blank=True, null=True)

class ChatGPTResponse(models.Model):
    response= models.CharField()
