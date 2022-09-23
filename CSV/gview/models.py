from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
        
    gender = models.CharField(max_length=1, choices= Gender.choices)

    def __str__(self):
        return self.name 
    
    def getGender(self):
        return Person.Gender(self.gender).label
    
    def getBirthdate(self):
        return self.birthdate.strftime("%d-%B-%Y")
        

