from django.urls import path
from .views import ImageListView, ExerciseResponseView, ExerciseResponseEditView, MealResponseView, MealResponseEditView, CreateResponseView, RunOCR

urlpatterns = [
    path('image/', ImageListView.as_view()),
    path('result/exercise/<int:user_id>', ExerciseResponseView.as_view()),
    path('result/exercise/edit/', ExerciseResponseEditView.as_view()),
    path('result/meal/<int:user_id>', MealResponseView.as_view()),
    path('result/meal/edit/', MealResponseEditView.as_view()),
    path('result/create/', CreateResponseView.as_view()),
    path('image/<int:image_id>/ocr/', RunOCR.as_view()),
]
