from rest_framework import serializers
from market.serializers.user_serilizator import UserProfileSerializer


class InitSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()
