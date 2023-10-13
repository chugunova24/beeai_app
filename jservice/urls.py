from django.urls import path, include

from . import views


urlpatterns = [
    path("random/", views.RandomQuestionAPIView.as_view()),
]
