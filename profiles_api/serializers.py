from rest_framework import serializers
from profiles_api import models

class HelloSerializers(serializers.Serializer):
    """serializers for test api view"""
    name=serializers.CharField(max_length=10)
    #age=serializers.IntegerField(max_value=None, min_value=None)

class UserProfileSerializer(serializers.ModelSerializer):
    """sericalser a user profile objects"""
    class Meta:
        model= models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={'password':{'write_only':True,'style':{'input_type':'password'}}}

    def create(self, validated_data):

        user = models.UserProfile.objects.create_user(email=validated_data['email'],
                                                      name=validated_data['name'],
                                                      password=validated_data['password'])

        user.save()
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
