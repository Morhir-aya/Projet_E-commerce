from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.
class product(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    Title=models.CharField(max_length=50)
    Price=models.DecimalField(max_digits=6,decimal_places=5)
    Description=models.TextField()
    Color=models.CharField(max_length=50,choices=SHIRT_SIZES)
    Quantite=models.DecimalField(max_digits=6,decimal_places=5)
    product_image= models.ImageField(null=True,blank=True, upload_to='static/images/shop/products')
    Taille=models.CharField(max_length=4,choices=SHIRT_SIZES)
    Present_Panier=models.BooleanField(default=False)
    
    def _str_(self):
        return self.Title