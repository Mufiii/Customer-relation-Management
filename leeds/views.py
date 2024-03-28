from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leeds.serializers import LeedListSerializer , LeedsPostSerializer
from authentication.models import User
from rest_framework import viewsets,permissions
from .models import Leed



class LeedsAPIView(APIView):
    def get(self,request):
        leeds = Leed.objects.all()
        serializer = LeedListSerializer(leeds,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # def post(self,request):
    #     serializer = LeedsPostSerializer(data=request.data)
        
    