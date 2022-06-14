from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, get_user_model

from .validators import PhoneNumberValidator, VerifyValidator


User = get_user_model()
UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    def validate(self, validated_data):
        phone_number = validated_data['phone_number']
        if not (validated_data['password'] == validated_data['password2']):
            raise ValidationError("Enter same password!")
        if phone_number:
            valid_digits = [920, 921, 922, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 990, 991, 992, 993, 994,
                            931, 932, 933, 934, '901', '902', '903', '904', '905', 930, 933, 935, 936, 937, 938, 939]
            phone_number_validator = PhoneNumberValidator(phone_number=phone_number,
                                                          valid_digits=valid_digits)
            validated_data['phone_number'] = phone_number_validator.phone_number_validator()
        elif not validated_data['email']:
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


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, validated_data):
        verify_validators = VerifyValidator(phone_number=self.phone_number, email=self.email)
        phone_number_is_active = verify_validators.phone_number_is_verified()
        email_is_active = verify_validators.email_is_verified()
        if validated_data['phone_number'] and validated_data['password']:
            if phone_number_is_active:
                user = authenticate(phone_number=validated_data['phone_number'],
                                    password=validated_data['password'])
            else:
                raise ValidationError('you should verify your phone number first')
        elif validated_data['email'] and validated_data['password']:
            if email_is_active:
                user = authenticate(email=validated_data['email'], password=validated_data['password'])
            else:
                raise ValidationError('you should verify your email first')
        else:
            raise ValueError('Must provide password and one of the phone number or email.')
        if user:
            if user.is_active:
                if not user.is_deleted:
                    validated_data["user"] = user
                else:
                    raise ValidationError("User account is not found.")
            else:
                raise ValidationError("User is deactivated.")
            return validated_data
        raise ValidationError("unable to login")

    class Meta:
        model = UserModel
        fields = ("phone_number", "password", 'email')
