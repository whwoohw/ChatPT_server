from django.urls import path
from .views import ImageListView, ExerciseResponseView, MealResponseView, CreateResponseView, CollectMetaData

urlpatterns = [
    path('image/', ImageListView.as_view()),
    path('result/exercise/<int:user_id>', ExerciseResponseView.as_view()),
    path('result/meal/<int:user_id>', MealResponseView.as_view()),
    path('result/create/', CreateResponseView.as_view()),
    path('metadata/', CollectMetaData.as_view())
]
