from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()
UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        if not (validated_data['password'] == validated_data['password2']):
            raise ValidationError("Enter same password!")
        elif not validated_data['phone_number'] and not validated_data['email']:
            raise ValidationError("Phone number or email must be set")
        return validated_data

    def create(self, validated_data):
        password = validated_data['password']
        phone_number = validated_data['phone_number']
        email = validated_data['email']

        if self.validate(validated_data):
            user = UserModel.objects.create_user(
                phone_number,
                email,
                password
            )
            return user
        else:
            raise ValidationError("Enter same password!")

    class Meta:
        model = UserModel
        fields = ("phone_number", "email", "password", "password2")


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("phone_number", "first_name", "last_name", "email")


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("phone_number", "email")


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("phone_number", "first_name", "last_name", "email", "date_joined")