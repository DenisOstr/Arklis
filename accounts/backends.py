from django.conf import settings
from .models import Account

class UserAuth(object):
	def authenticate(self, request, username = None, password = None):
		try:
			user = Account.objects.get(username = username)

			if user.check_password(password):
				return user
		except Account.DoesNotExist:
			return None


	def get_user(self, user_id):
		try:
			user = Account.objects.get(pk = user_id)

			if user.is_active:
				return user

			return None
		except Account.DoesNotExist:
			return None