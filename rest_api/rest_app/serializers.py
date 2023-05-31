from rest_framework import serializers
from rest_app.models import User
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_app.utils import Util


class UserSerializer(serializers.ModelSerializer):
    # We are writting this because we need confirm password field in our Registration Request
    password2 = serializers.CharField(style={"input-type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "password and confirm password doesn't match "
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError(
                "password and confirm password doesn't match "
            )
        user.set_password(password)
        user.save()
        return attrs


class EmailSendResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        print("attrs data ", attrs)
        print(type(attrs))
        email = attrs.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("Encoded UID", uid)
            print(user)
            token = PasswordResetTokenGenerator().make_token(user)
            print("Password Reset Token", token)
            link = "http://127.0.0.1:8000/api/reset_password/" + uid + "/" + token
            print("Password Reset link", link)
            print(attrs)
            # Send link to Email.
            body = "Click following link to Reset your password:" + link
            # print(body)
            data = {
                "subject": "Reset Your Password",
                "body": body,
                "to_email": user.email,
            }
            # print(data["to_email"])
            Util.send_email(data)
            return attrs
        else:
            raise ValidationError("You are not a Register user")


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, style={"input_type": "password"}, write_only=True
    )

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            password2 = attrs.get("password2")
            uid = self.context.get("uid")
            token = self.context.get("token")
            if password != password2:
                raise serializers.ValidationError(
                    "Password and Confirm Password doesn't match"
                )
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationError("Token is not valid or expired")
            user.set_password(password2)
            user.save()
            return attrs
        except (
            DjangoUnicodeDecodeError,
            ValueError,
        ):
            # PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationError("Token is not valid or expired")
