from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Patient(models.Model):
    Date=models.CharField(max_length=10)
    patients_name = models.CharField(max_length=100)

    patients_mobile = models.CharField(max_length=15)
    
    patients_age = models.CharField(max_length=10)
   
    Right_eye = models.CharField(max_length=50)
    Left_eye = models.CharField(max_length=50)
    frame = models.CharField(max_length=50)
    lenses= models.CharField(max_length=50)
   

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.patients_name

    

    def get_absolute_url(self):
        return reverse('patient_details', kwargs={'pk': self.pk})



