from django.contrib.auth.models import User
from .models import CustomUser

class PhoneNumberBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(phone_number=username)
            return user
        except Exception as e:
            return None
    
    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            return user
        except Exception as e:
            return None