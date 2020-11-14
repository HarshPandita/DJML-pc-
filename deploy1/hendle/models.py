
from django.db import models

# Create your models here.

class record(models.Model):
	name = models.CharField(max_length=200)
	Follicle_r=models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
	Follicle_l=models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
	Skin_darkening =models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
	hair_growth=models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
	Weight_gain=models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
	Cycle=models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)



	def __str__(self):
		return self.name
