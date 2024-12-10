from .models import CustomUser
from rest_framework.serializers import ModelSerializer


class CustomSerailizer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


        

    