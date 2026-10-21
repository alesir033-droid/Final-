
from typing import Iterable
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
#from ttgen.models import Room
from django.contrib.auth.models import Group
# Create your models here.
#from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import  Permission

# Create your models here.
from django.db import models
import math
import random as rnd
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
#from classschedulingApp.models import Instructor
time_slots = (
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('10:30 - 11:30', '10:30 - 11:30'),
    ('11:30 - 12:30', '11:30 - 12:30'),
    ('12:30 - 1:30', '12:30 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1



scheduler_group, created = Group.objects.get_or_create(name="Scheduler")
instructor_group, created = Group.objects.get_or_create(name="Instructor")





class User(AbstractUser):
    email = models.EmailField(blank=True,)
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email']
    phone = models.CharField(max_length=150, blank=True,help_text="Phone ")
    address = models.CharField(max_length=150, blank=True,help_text="address")
    student =  models.BooleanField(
       
        default=False,
        help_text=(
            "student"
        ),
    )
    departmenthead =  models.BooleanField(
       
        default=False,
        help_text=(
            "Department head"
        ),
    )
    instructor =  models.BooleanField(
       
        default=False,
        help_text=(
            "Instructor"
        ),
    )

    def __str__(self):
        return f"user: {self.email}"
class Student(models.Model):
    first_name= models.CharField(max_length=255, blank=True, help_text="First Name")
    last_name=models.CharField(max_length=255, blank=True, help_text="Last Name")
    username=models.CharField(max_length=255, blank=False, unique=True, help_text="User name")
    email = models.EmailField(max_length=255, blank=True, help_text="email")
    password =models.CharField(max_length=255,help_text="Password")
    phone = models.CharField(max_length=255, blank=True, help_text="Phone")
    address = models.CharField(max_length=150, blank=True,help_text="address")
    active =models.BooleanField(default=True)
    student= models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.username}"
    def save(self):
        new_Instructor=User.objects.create(first_name=self.first_name,
                            
                            last_name=self.last_name,
                            username=self.username,
                            email=self.email,
                            password= make_password(self.password),
                            phone= self.phone,
                            is_active =True,
                            student=True,
                            address=self.address,
                          
                            )
        new_Instructor.save()
        send_mail(
            subject = "Dear User",
             message = f"Please save securely you username:{self.username} and password:{self.password} of  Faculty of Computing and Informatics Class Scheduling System",
             recipient_list = (self.email,),
             from_email = None,
             fail_silently=False,
         )
        return super().save()
    
class Departmenthead(models.Model):
    first_name= models.CharField(max_length=255, blank=True, help_text="First Name")
    last_name=models.CharField(max_length=255, blank=True, help_text="Last Name")
    username=models.CharField(max_length=255, blank=False, unique=True, help_text="User name")
    email = models.EmailField(max_length=255, blank=True, help_text="email")
    password =models.CharField(max_length=255,help_text="Password")
    phone = models.CharField(max_length=255, blank=True, help_text="Phone")
    address = models.CharField(max_length=150, blank=True,help_text="address")
    active =models.BooleanField(default=True)
    departmenthead= models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.username}"
    def save(self):
        new_Instructor=User.objects.create(first_name=self.first_name,
                            
                            last_name=self.last_name,
                            username=self.username,
                            email=self.email,
                            password= make_password(self.password),
                            phone= self.phone,
                            is_active =True,
                            is_staff=True,
                            departmenthead=True,
                            address=self.address,
                          
                            )
        new_Instructor.save()
        send_mail(
            subject = "Dear User",
             message = f"Please save securely you username:{self.username} and password:{self.password} of  Faculty of Computing and Informatics Class Scheduling System",
             recipient_list = (self.email,),
             from_email = None,
             fail_silently=False,
         )
        return super().save()
class Instructors(models.Model):
    
    first_name= models.CharField(max_length=255, blank=True, help_text="First Name")
    last_name=models.CharField(max_length=255, blank=True, help_text="Last Name")
    
    name= models.CharField(max_length=255, blank=True, help_text="Full Name")
    username=models.CharField(max_length=255, blank=False, unique=True, help_text="User name")
    email = models.EmailField(max_length=255, blank=True, help_text="email")
    password =models.CharField(max_length=255,help_text="Password")
    phone = models.CharField(max_length=255, blank=True, help_text="Phone")
    address = models.CharField(max_length=150, blank=True,help_text="address")
    active =models.BooleanField(default=True)
    instructor= models.BooleanField(default=True)
    
    
    def __str__(self):
        return f'{self.name}'
    def save(self):
        self.name= f'{self.first_name} {self.last_name}' 
        new_Instructor=User.objects.create(first_name=self.first_name,
                            
                            last_name=self.last_name,
                            username=self.username,
                            email=self.email,
                            password= make_password(self.password),
                            phone= self.phone,
                            is_active =True,
                            instructor=True,
                            is_staff=True,
                            address=self.address,
                          
                            )
        new_Instructor.save()
        send_mail(
            subject = "Dear User",
             message = f"Please save securely you username:{self.username} and password:{self.password} of  Faculty of Computing and Informatics Class Scheduling System",
             recipient_list = (self.email,),
             from_email = None,
             fail_silently=False,
         )
        return super().save()
    
class Administrator(models.Model):
    first_name= models.CharField(max_length=255, blank=True, help_text="First Name")
    last_name=models.CharField(max_length=255, blank=True, help_text="Last Name")
    username=models.CharField(max_length=255, blank=False, unique=True, help_text="User name")
    email = models.EmailField(max_length=255, blank=True, help_text="email")
    password =models.CharField(max_length=255,help_text="Password")
    phone = models.CharField(max_length=255, blank=True, help_text="Phone")
    address = models.CharField(max_length=150, blank=True,help_text="address")
    active =models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.username}"
    def save(self):
        new_Instructor=User.objects.create(first_name=self.first_name,
                            
                            last_name=self.last_name,
                            username=self.username,
                            email=self.email,
                            password= make_password(self.password),
                            phone= self.phone,
                            is_active =True,
                            instructor=False,
                            is_staff=True,
                            address=self.address,
                          
                            )
        new_Instructor.save()
        send_mail(
            subject = "Dear User",
             message = f"Please save securely you username:{self.username} and password:{self.password} of  Faculty of Computing and Informatics Class Scheduling System",
             recipient_list = (self.email,),
             from_email = None,
             fail_silently=False,
         )
        return super().save()









class FeedBack(models.Model):
    date = models.DateField(auto_now=True)
    name= models.CharField(max_length=255, help_text="Name")
    email = models.EmailField(max_length=255, help_text="email")
    student= models.BooleanField(default=False)
    
    instructor= models.BooleanField(default=False)
    subject= models.CharField(max_length=255, help_text="Subject")
    message = models.TextField(max_length=3000, help_text="message")

    def __str__(self):
        return f"Feed Back from {self.name}"
    

class Notification(models.Model):
    date = models.DateField(auto_now=True)
    updated = models.BooleanField(default=False)
    notify = models.IntegerField(default=1)
    
    
class Attendance(models.Model):
    date = models.DateTimeField(auto_now=True)
    student= models.ForeignKey(Student, on_delete=models.SET_NULL,null=True, blank=True)
    morning = models.DateTimeField()
    attend_at_morning= models.BooleanField(default=False) 
    afternoon = models.DateTimeField()
    attend_at_afternoon= models.BooleanField(default=False) 
    
    


   





    













