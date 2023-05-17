import json
import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from django.core import serializers
from rest_framework.response import Response
from django.forms.models import model_to_dict

LOGGER = logging.getLogger(__name__)

class SignUpAPI(APIView):

    def __init__(self, **kwargs):
        super(SignUpAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    def get(self, request):
        LOGGER.debug("This is get")
        return render(request, "signup.html")