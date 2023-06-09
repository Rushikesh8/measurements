from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class SignInSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email","username","password","first_name","last_name"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self,validated_data):
        password = validated_data.pop("password",None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance