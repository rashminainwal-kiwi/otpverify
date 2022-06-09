from rest_framework import serializers, validators
from django.contrib.auth.models import User

import validation_message

'''  authentication serializer  '''


class RegistrationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True, min_length=validation_message.CHAR_LIMIT_SIZE['name_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['name_max'],
        error_messages=validation_message.VALIDATION['name']
    )

    email = serializers.EmailField(required=True, error_messages=validation_message.VALIDATION['email'])

    username = serializers.CharField(
        min_length=validation_message.CHAR_LIMIT_SIZE['username_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['username_max'],
        error_messages=validation_message.VALIDATION['username']
    )

    password = serializers.CharField(
        min_length=validation_message.CHAR_LIMIT_SIZE['password_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['password_max'],
        error_messages=validation_message.VALIDATION['password'],
        write_only=True)

    password2 = serializers.CharField(
        min_length=validation_message.CHAR_LIMIT_SIZE['password_min'],
        max_length=validation_message.CHAR_LIMIT_SIZE['password_max'],
        error_messages=validation_message.VALIDATION['password2'],
        write_only=True)

    otp = serializers.CharField(max_length=6)
    is_active = serializers.BooleanField(default=False)

    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'username', 'password', 'password2', 'is_active', 'otp')

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("password does not match")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            # name=validated_data["name"],
            email=validated_data["email"],
            # otp=validated_data["otp"],
        )

        user.set_password(validated_data["password"])
        user.save()

        # Validating Password and Confirm Password while Registration
#
# def validate_password(password_value):
#     password_value = password_value.strip()
#     if password != password2.:
#          return "email is alrea"


# def validate_email(email_value):
#     email_value = email_value.strip()
#     if email_value.exists():
#         return email_value
#     raise serializers.ValidationError({'email': 'email already exists'})


# def validate(self, args):
#     email = args.get('email', None)
#     username = args.get('username', None)
#     password = args.get('password', None)
#     if User.objects.filter(email=email).exists():
#         raise serializers.ValidationError({'email': 'email already exists'})
#     if User.objects.filter(username=username).exists():
#         raise serializers.ValidationError({'username': 'username already exists'})
#     if args['password'] < 16:
#         raise serializers.ValidationError({'error': "password must be less than 16"})
#     if args['name']:
#         for n in args['name']:
#             if n.isdigit():
#                 raise serializers.ValidationError({'error': "name can not be numeric"})
#
#     return super().validate(args)
