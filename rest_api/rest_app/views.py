from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_app.serializers import (
    UserSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
    EmailSendResetPasswordSerializer,
    UserPasswordResetSerializer,
)
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import requests
from rest_app.models import User


# Creating token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # get_tokens_for_user(user)
        return Response(
            {"success": "Registered succesfully"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    # logout(request)
    # print(request.user)
    # return Response({"msg": "hfhajfajsfh"})
    serializer = UserLoginSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        email = serializer.data.get("email")
        print(email)
        password = serializer.data.get("password")
        print(password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            # login(request, user)
            # requests.post(
            #     "http://localhost:8000/api/token/",
            #     data={"email": "vinesh@gmail.com", "password": "Vinesh@309"},
            # )
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "success": "User authenticated succesfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"errors": {"non_field_errors": ["email or password is not valid"]}},
                status=status.HTTP_404_NOT_FOUND,
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def profile(request):
    # user = User.objects.get(id=2)
    # login(request, user)
    # logout(request)
    serializer = UserProfileSerializer(request.user)
    # if serializer.is_valid():
    return Response(serializer.data, status=status.HTTP_200_OK)
    # return JsonResponse(serializer.data)
    # if request.headers.get("Authorization"):
    #     if request.headers.get("Authorization").startswith("Bearer"):
    #         return JsonResponse({"success": "success"}, status=status.HTTP_200_OK)
    #     else:
    #         return JsonResponse(
    #             {"fail": "authorization token should start with Bearer"}, status=401
    #         )
    # else:
    #     return JsonResponse({"fail": "enter proper header"}, status=401)

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def change_password(request):
    # permission_classes = [IsAuthenticated]
    serializer = UserChangePasswordSerializer(
        data=request.data, context={"user": request.user}
    )
    if serializer.is_valid(raise_exception=True):
        return Response(
            {"success": "password changed successfully"}, status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def email_send_reset_password(request):
    # print(request.data)
    # print(type(request.data))
    serializer = EmailSendResetPasswordSerializer(data=request.data)
    # print(serializer.initial_data)
    # print(type(serializer.initial_data))
    print(serializer.is_valid())
    if serializer.is_valid(raise_exception=True):
        # print(serializer.validated_data)
        # print(type(serializer.validated_data))
        return Response(
            {"success": "Password Reset link send.Please check your Email"},
            status=status.HTTP_200_OK,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_password_reset(request, uid, token):
    serializer = UserPasswordResetSerializer(
        data=request.data, context={"uid": uid, "token": token}
    )
    if serializer.is_valid(raise_exception=True):
        return Response(
            {"success": "Password Reset Successfully"}, status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
