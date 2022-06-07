from django.db import models

# Create your models here.
class users(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.email

class inscrip(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.email