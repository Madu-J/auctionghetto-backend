from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializer.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = '__all__'
