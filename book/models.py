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
	TYPE = (
		('IN',	'Income'),
		('EX',	'Expence'),
	)
	verification_number = models.AutoField(
		primary_key = True,
		)
	verification_date = models.DateField()
	expiration_date = models.DateField()
	verification_type = models.CharField(
		max_length = 25,
		choices = TYPE,
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
		return str(self.creation_date) + " - " + str(self.verification_desc)

class Transaction(models.Model):
	verification = models.ForeignKey(
		Verification
		)
	transaction_date = models.DateField()
	entry_date = models.DateField(
		auto_now = True
		)
	class Meta:
		verbose_name = ('Transaction')
		verbose_name_plural = ('Transactions')

	def __unicode__(self):
		pass
    
class Entry(models.Model):
	TYPE = (
		('DEBIT', 'Debit'),
		('CREDIT', 'Credit')) 
	transaction = models.ForeignKey(
		Transaction
		)
	account = models.ForeignKey(
		Account
		)
	entry_type = models.CharField(
		max_length = 20,
		choices = TYPE,
		)
	entry_sum = models.FloatField()

	class Meta:
		verbose_name = ('entry')
		verbose_name_plural = ('entrys')

	def __unicode__(self):
		pass
    