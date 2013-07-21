from django.db import models

# Create your models here.
class Account(models.Model):
	account_number = models.IntegerField(
		primary_key = True,
		)
	account_name = models.CharField(
		max_length = 255,
		)
	account_description = models.TextField(
		max_length = 400,
		)

	def __str__(self):
		
		return ' '.join([
			self.account_number,
			self.account_name,
		])