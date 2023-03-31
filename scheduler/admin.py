from django.contrib import admin
from .models import InbodyImage, ChatGPTResponse

# Register your models here.
admin.site.register(InbodyImage)
admin.site.register(ChatGPTResponse)