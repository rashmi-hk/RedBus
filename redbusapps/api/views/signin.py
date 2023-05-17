from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from ...models import CustomUser


class SignInAPI(APIView):

    def __init__(self, **kwargs):
        super(SignInAPI, self).__init__(**kwargs)
        self.User = get_user_model()

    def get(self, request):
        print("This is get signin")
        return render(request, 'signin.html')

    def post(self, request):
        print("Inside post signin",request.data)
        username = request.data["username"]
        password = request.data["password"]

        print("username", username)
        print("password", password)

        user = CustomUser.objects.get(email=username)
        print("user", user)

        if user:
           context = {'success_message': 'Login successful!'}
        else:
            context = {'error_message': 'Invalid credentials!'}
        
        print("password, username", username,password)
        print("*******************")
        return render(request, 'signin.html',context)