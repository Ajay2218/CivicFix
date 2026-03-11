from django.db import models

# Create your models here.


class AddcategoryDb(models.Model):
    Category_name = models.CharField(max_length=100,null=True,blank=True)
    
