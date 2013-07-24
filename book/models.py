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
		
		return self.account_name

class Verification(models.Model):
	verification_number = models.AutoField(
		primary_key = True,
		)
	verification_date = models.DateField()
	expiration_date = models.DateField()
	verification_type = models.CharField(
		max_length = 25
		)
	verification_desc = models.CharField(
		max_length = 50
		)
	creation_date = models.DateField(
		auto_now_add = True
		)
	last_edit_date = models.DateField(
		auto_now = True
		)
	class Meta:
		verbose_name = ('Verification')
    	verbose_name_plural = ('Verifications')

	def __unicode__(self):
		pass
    