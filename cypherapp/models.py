from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .utils import *

# Create your models here.
class Client(models.Model):
	GENDER= (
		('MALE', 'MALE'),
		('FEMALE', 'FEMALE'),
		('TRANSGENDER', 'TRANSGENDER'),
		('RATHER NOT SAY', 'RATHER NOT SAY'),
		)
	KIN_GENDER= (
		('MALE', 'MALE'),
		('FEMALE', 'FEMALE'),
		('TRANSGENDER', 'TRANSGENDER'),
		('RATHER NOT SAY', 'RATHER NOT SAY'),
		)
	RELATIONSHIP=(
		('FATHER', 'FATHER'),
		('MOTHER', 'MOTHER'),
		('SIBLING', 'SIBLING'),
		('SPOUSE', 'SPOUSE'),
		('OTHERS', 'OTHERS'),
		)
	user= models.OneToOneField(User, on_delete= models.CASCADE)
	bio= models.TextField(blank= True)
	first_name= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	last_name= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	email_address= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	country= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	city= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	home_address= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	Date_of_birth= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	gender= models.CharField(max_length=64, default='update your account', null=True, blank=True, choices=GENDER)
	occupation= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	monthly_income= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	reason_for_investing= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	code= models.CharField(max_length=12, blank=True)
	recommended_by= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
	updated= models.DateTimeField(auto_now= True)
	created= models.DateTimeField(auto_now_add= True)
	deposit= models.FloatField(default=0, null=True)
	balance= models.FloatField(default=0,null=True)
	withdrawal= models.FloatField(default=0,null=True)
	profit= models.FloatField(default=0,null=True)
	roi= models.FloatField(default=0.015, null=True)
	investment_plan_name= models.CharField(default='MISSED-INFO', max_length=20, null=True, blank=True)
	contract_duration= models.FloatField(default=180, null=True, blank=True)
	running_days= models.IntegerField(default=0, null=True)
	wallet_address= models.CharField(max_length=400, default='update your account', null=True)
	ID_CARD= models.ImageField(null=True, blank=True)
	next_of_kin_fullname= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	next_of_kin_phonenumber= models.CharField(max_length=64, default='update your account', null=True, blank=True)
	next_of_kin_gender= models.CharField(max_length=64, default='update your account', null=True, blank=True, choices=KIN_GENDER)
	next_of_kin_age= models.CharField(max_length=64, default='update your account', null=True, blank=True,)
	next_of_kin_phonenumber= models.CharField(max_length=64, default='update your account', null=True, blank=True,)
	next_of_kin_home_address= models.CharField(max_length=64, default='update your account', null=True, blank=True,)
	relationship_status_with_next_of_kin= models.CharField(max_length=64, default='update your account', null=True, blank=True, choices=RELATIONSHIP)

	def __str__(self):
		return f'{self.user.username}-{self.code}'

	@property
	def profile_picUrl(self):
		try:
			url= self.profile_pic.url
		except:
			url=''
		return url

	def get_recommended_profiles(self):
		query= Client.objects.all()
		my_recs= []
		for i in query:
			if i.recommended_by== self.user:
				my_recs.append(i)
		return my_recs


	def save(self, *args, **kwargs):
		if self.code=='':
			code= generate_ref_code()
			self.code= code
		super().save(*args, **kwargs)


class Payment_id(models.Model):
	client= models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
	payment_id= models.CharField(max_length=200, null=True)
	price_amount= models.CharField(max_length=200, null=True)
	investment_plan= models.FloatField(default=0.0052, null=True)
	investment_plan_name= models.CharField(default='MISSED-INFO', max_length=20, null=True, blank=True)
	contract_duration= models.FloatField(default=180, null=True, blank=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return f'{self.client.user.username}'

class Plan(models.Model):
	investment_name= models.CharField(max_length=64, null=True, blank=True)
	mimimum_amount= models.FloatField(default=0, null=True, blank=True)
	maximum_amount= models.FloatField(default=0, null=True, blank=True)
	return_of_investment= models.CharField(max_length=5000, null=True, blank=True)
	duration= models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return self.investment_name

class Notification(models.Model):
	client= models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
	message_subject= models.CharField(max_length=200, blank=True, null=True)
	message_body= models.TextField(max_length=1500, blank=True, null=True)
	created= models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return f'{ self.client.user.username} - {self.message_subject }'

class Withdrawal_request(models.Model):
	client= models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
	client_username= models.CharField(max_length=200, null=True)
	client_email= models.CharField(max_length=200, null=True)
	transaction_hash= models.CharField(max_length=20, null=True,)
	crypto_used_for_requesting_withdrawal= models.CharField(max_length=35, null=True)
	withdrawal_address= models.CharField(max_length=200, null=True)
	amount= models.FloatField(default=0, null=True)
	date_created= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.client_username

	def save(self, *args, **kwargs):
		if self.transaction_hash == "":
			transaction_hash= transaction_hash_code()
			self.transaction_hash = transaction_hash
		super().save(*args, **kwargs)

class Transaction(models.Model):
	client= models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
	transaction_type= models.CharField(max_length=64, null=True, blank=True)
	transaction_id= models.CharField(max_length=30, null=True, blank=True, default='504ID.omit')
	investment_plan= models.CharField(max_length=64, null=True, blank=True, default='504Package.omit')
	amount= models.FloatField(default=0, null=True)
	status= models.CharField(max_length=64, null=True, blank=True)
	created= models.DateTimeField(auto_now_add= True, null=True, blank=True)
	def __str__(self):
		return self.client.user.username

class Bonus(models.Model):
	client= models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
	transaction_type= models.CharField(max_length=64, null=True, blank=True, default='Pending Bonus')
	amount= models.FloatField(default=0, null=True)
	code= models.CharField(max_length=8, null=True, blank=True, unique=True)
	client_email= models.CharField(max_length=68, null=True, blank=True)
	message= models.TextField(max_length=1000, null=True, blank=True)
	created= models.DateTimeField(auto_now_add= True, null=True, blank=True)
	def __str__(self):
		return self.client.user.username

class Minimum_withdrawal(models.Model):
    minimum_withdrawal= models.FloatField(default=0)

    def __str__(self):
        return f"Your minimum withdrawal goes here"

class Maximum_withdrawal(models.Model):
    maximum_withdrawal= models.FloatField(default=0)

    def __str__(self):
        return f"Your maximum withdrawal goes here"

class Video(models.Model):
	meeting_agenda= models.CharField(max_length=68, null=True, blank=True, default="Live Video")
	video = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
	date_uploaded = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return f" {self.meeting_agenda} - Only post one video at a time. Delete then post another one."

class Package(models.Model):
	package_name= models.CharField(max_length=68, null=True, blank=True)
	percentage_return= models.DecimalField(null=True, blank=True, max_digits=19, decimal_places=10)
	maximum_amount= models.FloatField(default=0, null=True)
	minimum_amount= models.FloatField(default=0, null=True)

	def __str__(self):
		return f"{self.package_name}"



