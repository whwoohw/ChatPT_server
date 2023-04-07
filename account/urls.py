from django.urls import path
from .views import SignUp, Login, Logout

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
]
