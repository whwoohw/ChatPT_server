from django.urls import path
from .views import ImageList, ExerciseResponseList, ExerciseResponseEdit, MealResponseList, MealResponseEdit, CreateResponse, RunOCR

urlpatterns = [
    path('image/', ImageList.as_view()),
    path('result/exercise/', ExerciseResponseList.as_view()),
    path('result/exercise/edit/', ExerciseResponseEdit.as_view()),
    path('result/meal/', MealResponseList.as_view()),
    path('result/meal/edit/', MealResponseEdit.as_view()),
    path('result/create/', CreateResponse.as_view()),
    path('image/<int:image_id>/ocr/', RunOCR.as_view())
]
