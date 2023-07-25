from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



@api_view(["GET"])
def index(request):
    return Response({"sucess": "your data has been recived"})


@api_view(["POST", "GET"])
def create_admin(request):
    searializer = UserSerializer(data=request.data)
    if searializer.is_valid():
        searializer.save()
        return Response(
            {"sucess": "the data has been successfull stored"},
            status=status.HTTP_200_OK,
        )
    return Response(searializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["POST", "GET"])
def login_user(request):
    if request.method == "POST":
        data = request.data
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(
                {
                    "message": "Login successful",
                    "userId": user.id,
                    "sessionKey": request.session.session_key,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "message": "Invalid Credentials",
                },
                status=401,
            )
    else:
        return Response(
            {"message": "Invalid request method"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )


@api_view(["POST", "GET"])
def logout(request):
    if request.method == "POST":
        try:
            logout(request)
            return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)
        except NameError as e:
            return Response({"message": "WE FOUND THE ERROR LOGGING YOU OUT {e}"})
    return Response(
        {"message": "Invalid method type"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def validate_token(request):
    return Response({"message": "Token is valid"})
