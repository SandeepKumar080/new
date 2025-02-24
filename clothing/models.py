from django.db import models

# Create your models here.
class product(models.Model):
    size_choices=[
        ('s','Small'),
        ('m','Medium'),
        ('L','Large'),
        ('XL','Extra Large')
    ]
    
    colour_choices=[
        ('Red','Red'),
        ('Blue','Blue'),
        ('White','White'),
        ('Black','Black'),
    ]
    
    name= models.CharField(max_length=200)
    size=models.CharField(max_length=2, choices=size_choices,default='m')
    colour=models.CharField(max_length=10, choices=colour_choices,default='Black')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='product_img/')