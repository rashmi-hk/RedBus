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
