from django.urls import path
from .views import ImageList, ResponseList

urlpatterns = [
    path('image/', ImageList.as_view()),
    path('result/', ResponseList.as_view())
]
