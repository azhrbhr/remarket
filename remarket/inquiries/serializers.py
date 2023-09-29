from products.serializers import ProductSerializer
from rest_framework import serializers
from interests.models import Interest
from rest_framework.fields import CurrentUserDefault
from authentications.serializers import UserSerializer


class InquirySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    created_at = serializers.DateTimeField(
        format='%A, %B %d, %Y %I:%M %p')

    class Meta:
        model = Interest
        fields = '__all__'
