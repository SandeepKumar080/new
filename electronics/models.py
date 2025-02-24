from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    
    def _str_(self):
        return self.name
    