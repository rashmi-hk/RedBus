from django.urls import path
from redbusapps.api.views.bus import BusAPIList
from redbusapps.api.views.signup import SignUpAPI
from redbusapps.api.views.signin import SignInAPI
from redbusapps.api.views.home import HomeAPI

urlpatterns = [
    path('bus/', BusAPIList.as_view()),
    path('signin/', SignInAPI.as_view()),
    path('signup/', SignUpAPI.as_view()),
    path('bus/<int:id>', BusAPIList.as_view()), 
    path('index/', HomeAPI.as_view()), 
   
    
    ]