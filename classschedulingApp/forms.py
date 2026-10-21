from django.forms import ModelForm
from classschedulingApp.models import *
from django import forms 

    
class InstructorForm(ModelForm):
    class Meta:
        model = Instructors
        
        fields = [
            #'uid',
            'username','email','first_name','last_name','password','phone','address','active','instructor'
        ]