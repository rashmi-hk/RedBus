from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model

from .manager import UserManager
from  cloudinary.models import CloudinaryField

# User = get_user_model()

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField('Bus_Name',max_length=100)
    bus_number = models.IntegerField('Bus_Number')
    start_point = models.CharField('start_point',max_length=100)
    destination = models.CharField('destination',max_length=100)
    arrival_time = models.DateTimeField('Arrival_Time')
    departure_time = models.DateTimeField('Departure_Time')
    bus_image = CloudinaryField(blank=False)
    seatlimit = models.IntegerField('Seat_Limit')

    def __str__(self):
        return "{0} | {1} | {2} | {3}".format(self.bus_name, self.bus_number, self.start_point, self.destination)

    class Meta:
        db_table = 'Bus'



class CustomUser(AbstractUser):

    username = models.CharField('username',max_length=100)
    phone_number = models.CharField('phone_number',unique=True,max_length=10)
    user_bio = models.CharField('user_bio',max_length=100)
    email = models.EmailField(unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'CustomUser'

class Seat(models.Model):
    bus = models.ForeignKey(Bus, related_name= 'related_bus',blank=True, null=True,on_delete=models.SET_NULL)
    seat_name = models.CharField('Seat',max_length=5,blank=False,null=False,default=None)
    seat_number = models.CharField('Seat Number',max_length=5,null=False,blank=False,default=None)
    

    class Meta(object):
        db_table = 'seat'
        verbose_name = ('seat')

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
