from django.db import models

# Create your models here.

class Location(models.Model):

	location_name = models.CharField(max_length=50)
	postal_code = models.IntegerField()

	def __str__(self):
		return self.location_name + ' , ' + str(self.postal_code)

class Restaurant(models.Model):
	restaurant_location = models.ForeignKey(Location, on_delete=models.CASCADE)
	restaurant_name = models.CharField(max_length=50)
	restaurant_description = models.CharField(max_length=200)
	restaurant_link = models.URLField()
	
	#restaurant_logo = models.

	def __str__(self):
		return self.restaurant_name
