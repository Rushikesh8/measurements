from utils.base_view import BaseView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from utils.helpers import api_error_response,api_success_response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import SignInSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny 
from accounts.db_api import (create_userprofile,)

class SignInView(BaseView):
    permission_classes=(AllowAny,)

    def post(self,request):
        self.validate_field_in_params(request.data,["username","password","email"]) #As for Django User Email is non mandatory field so make it mandatory here
        signin_serializer = SignInSerializer(data=request.data)

        if signin_serializer.is_valid():
            user_instance = signin_serializer.save()
            if user_instance:
                create_userprofile(user=user_instance)
                token,_ = Token.objects.get_or_create(user=user_instance)
                return api_success_response(response_data={"auth_token": f"Token {str(token)}"},status=status.HTTP_201_CREATED)

        return api_error_response(errors=signin_serializer.errors)

class GetTokenView(BaseView):
    permission_classes=(AllowAny,)

    def get(self,request):
        self.validate_field_in_params(request.data,["username","password"])

        try:
            user_instance = User.objects.get(username=request.data["username"].strip())
        except ObjectDoesNotExist:
            return api_error_response(error_message=f"user for username {request.data['username']} does not exist")

        if not check_password(request.data["password"].strip(), user_instance.password):
            return api_error_response(error_message=f"Incorrect Password !")

        token,_ = Token.objects.get_or_create(user=user_instance)

        return api_success_response(response_data={
            "auth_token": f"Token {str(token)}"
        })

