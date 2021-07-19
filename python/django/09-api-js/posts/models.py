from django.db import models

# Create your models here.
class feed(models.Model):
	id=models.IntegerField(primary_key=True)
	author=models.CharField(max_length=50)
	title=models.CharField(max_length=100)
	body=models.TextField()

class meter(models.Model):
	id 			= models.BigAutoField(primary_key=True)
	time_from 	= models.DateTimeField(unique=True)
	consumption = models.DecimalField(null=True, max_digits=7, decimal_places=3)
	value		= models.DecimalField(null=True, max_digits=7, decimal_places=4)
