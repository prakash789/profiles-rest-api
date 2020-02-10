from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """serializers for test api view"""
    name=serializers.CharField(max_length=10)
    age=serializers.IntegerField(max_value=None, min_value=None)
