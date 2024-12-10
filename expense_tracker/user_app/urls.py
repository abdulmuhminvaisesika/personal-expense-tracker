from django.urls import path


from .views import CustomUserView


urlpatterns = [
    path('users/', CustomUserView.as_view()),
]