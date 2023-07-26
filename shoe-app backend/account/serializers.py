from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id','username','password','is_manager', 'is_employee', 'is_admin','first_name', 'last_name',  'email', 'phone_number'