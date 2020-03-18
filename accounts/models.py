from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
	def createUser(self, username, password, **extra_fields):
		if not username:
			raise ValueError('Users must have an username address')

		user = self.model(username = username)
		user.set_password(password)
		user.save(using = self._db)
		return user


class Account(AbstractBaseUser):
	# user = models.OneToOneField(User, on_delete = models.CASCADE)
	firstName = models.CharField(max_length = 255)
	lastName = models.CharField(max_length = 255)
	username = models.CharField(max_length = 255, unique = True)
	email = models.EmailField(max_length = 255)
	# password = models.CharField(max_length = 255)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['firstName', 'lastName', 'email']

	objects = UserManager()


	def __str__(self):
		return self.username