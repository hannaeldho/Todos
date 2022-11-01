from rest_framework import serializers

from django.contrib.auth.models import User
# create model serializers
from API.models import Todos


class TodoSerializer(serializers.ModelSerializer):
    status=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["task_name","user","status"]

    def create(self, validated_data):
        us=self.context.get("user")
        return Todos.objects.create(**validated_data,user=us)

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

# this function can overide create method in model serializer.this function not in the meta class
    def create(self,validated_data):
            return User.objects.create_user(**validated_data)