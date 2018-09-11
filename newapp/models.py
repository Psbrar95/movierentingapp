from django.db import models



# Create your models here.
class Movies(models.Model):
	name = models.CharField(max_length= 150)
	genre= models.CharField(max_length= 30)
	price= models.DecimalField(max_digits=6, decimal_places=2)
	year = models.IntegerField()
	isRented= models.BooleanField(default=False)
	def __str__(self):
		return self.name

class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number= models.CharField(max_length=40,null=True)
	address   = models.CharField(max_length= 300,null=True)
	email     = models.CharField(max_length= 100,null=True)
	movie = models.ForeignKey(Movies,on_delete=models.CASCADE,null = True,blank = True)

	def __str__(self):
		return self.first_name +" "+ self.last_name
