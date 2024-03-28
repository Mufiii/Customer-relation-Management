from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import AdminSerializer , AdminloginSerializer
from authentication.models import User
from authentication.utills.token import get_tokens_for_user
from django.contrib.auth import authenticate , login




class AdminRegistrationAPIView(APIView):
  def post(self,request):
      serializer = AdminSerializer(data=request.data)
      if serializer.is_valid():
        user = User.objects.create_user(
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'],
        )
        user.save()
        return Response({
          "msg":"User registered Successfully"},
          status=status.HTTP_200_OK
        )
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
      
# class AdminLoginAPIView(APIView):
#   def post(self, request):
    
#     serializer = AdminloginSerializer(data= request.data)
#     print(serializer)
#     print("hiiii")
#     if serializer.is_valid():
#       print(serializer.data)
#       email = serializer.data.get('email')
#       password = serializer.data.get('password')
#       existing_user = User.objects.filter(email=email).first()
#       print(existing_user,'222')
#       if existing_user:
              
#               user = authenticate(request, email=email, password=password)
#               if user is not None:
#                   login(request, user)
#                   token = get_tokens_for_user(user)
#                   return Response({"msg": "User Logged in Successfully", "token": token}, status=status.HTTP_200_OK)
#               else:
#                   # Incorrect password for existing user
#                   return Response({"msg": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
#       else:
#               # User with this email does not exist
#               return Response({"msg": "User with this email address does not exist"}, status=status.HTTP_404_NOT_FOUND)
#     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
      
class AdminLoginAPIView(APIView):
    def post(self,request):
      # print(request.data)
      serializer = AdminloginSerializer(data = request.data)
      if serializer.is_valid():
        print(serializer.data,'1111')
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        print(email,']]]]]')
        print(password,'[[[[[[[[]]]]]]]]')
        user = authenticate(request , email=email,password=password)
        print(user,'999')
        if user is not None:
          #  login(request,user)
           token = get_tokens_for_user(user)
           return Response({"msg":"User Loggined Successfully","token":token},status=status.HTTP_200_OK)
        else:
          return Response({"msg":"User not found"},status=status.HTTP_404_NOT_FOUND)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)