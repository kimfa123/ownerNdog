from django.db import models

# Create your models here.
class Owner(models.Model):
	name  = models.CharField(Max_lengh=45)
	email = models.CharField(Max_lengh=300)
	age   = models.IntegerField()
    
        class Meta:
    	    db_table = 'owners'
        
class Dog(models.Model):
	owners = models.Foreignkey(Owner, on_delet=models.CASCADE)
	name   = models.CharField(Max_lengh=45)
	age    = models.IntegerField()
    
        class Meta:
    	    db_table = 'dogs'