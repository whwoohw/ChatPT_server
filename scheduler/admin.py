from django.contrib import admin
from .models import InbodyImage, ExerciseResponse, MealResponse

# Register your models here.
admin.site.register(InbodyImage)
admin.site.register(ExerciseResponse)
admin.site.register(MealResponse)