from django.shortcuts import render
from rest_framework import status

from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# Create your views here.


class GoogleAuthAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer
    """
    POST with "auth token"
    sends an id token from google to get user details
    """
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data['auth_token'])
        return Response(data, status=status.HTTP_200_OK)
