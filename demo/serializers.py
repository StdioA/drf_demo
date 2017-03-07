from .models import Data
from rest_framework.serializers import ModelSerializer


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ("id", "content")
