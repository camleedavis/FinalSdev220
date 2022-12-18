from django.db import models

#pk 1 
# Create your models here.
class Customers(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length =250)
    
    def __str__(self):
        return self.firstname + '-' + self.lastname

class CustomerData(models.Model):
    address = models.CharField(max_length= 200, null =False )
    phone_num = models.IntegerField(max_length=10, null =False)
    card_num = models.IntegerField(max_length=12, null = False)
    def __str__(self):
        return self.address 

    
    
    
    
    
        