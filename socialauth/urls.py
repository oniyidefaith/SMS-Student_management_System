from django.urls import path
from .views import *

urlpatterns = [
    path('google', GoogleAuthAuthView.as_view()),
]
