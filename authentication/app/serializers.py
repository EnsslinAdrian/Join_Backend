from rest_framework import serializers
from authentication.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']

class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password' : { 'write_only': True }
            }
        
    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        em = self.validated_data['email']
        username = self.validated_data['username']

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('error', 'A user with that username already exists.')

        if User.objects.filter(email=em).exists():
            raise serializers.ValidationError({'error': 'A user with that Email already exists.'})

        if pw != repeated_pw:
            raise serializers.ValidationError({'error': 'Password dont match'})
    
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account