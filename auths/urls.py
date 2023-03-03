from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
