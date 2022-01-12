from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.[a-zA-Z0-9]+@(gmail|email|outlook|ctdtechs)+.(com|edu|net), #validators=[RegexValidator(r'^(0|91)?[6789][0-9]{9}$')]
# ,===,validators=[RegexValidator(r'^[a-zA-Z0-9]+@(gmail|email|outlook|ctdtechs)+.(com|edu|net)$')]
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nickname = models.CharField(max_length=200, null=True)
	phone= models.CharField(max_length=20,null=True,validators=[RegexValidator(r'^(0|91)?[6789][0-9]{9}$')])
	email = models.CharField(max_length=200,null=True,validators=[RegexValidator(r'^[a-zA-Z0-9]+@(gmail|email|outlook|ctdtechs)+.(com|edu|net)$')])
	profile_pic = models.ImageField(default="defaultpic.png",null=True, blank=True,)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.nickname

class diplayusername(models.Model):
	username=models.CharField(max_length=100)

