from rest_framework import serializers
from market.serializers.product import ProductSerializer


class BasketRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1))
