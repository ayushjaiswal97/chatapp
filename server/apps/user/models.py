from django.db import models
from django.contrib.auth.models import AbstractUser
import shortuuid

class User(AbstractUser):
	userId = models.CharField(max_length=22, unique=True, editable=False, default=shortuuid.uuid)
	image = models.ImageField(upload_to="user")

class OnlineUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
