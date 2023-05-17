from django.urls import path
from redbusapps.api.views.bus import BusAPIList



urlpatterns = [
    path('bus/', BusAPIList.as_view())]