from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': serializer.data, 'success': True, 'status_code': status.HTTP_200_OK})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'success': True, 'status_code': status.HTTP_201_CREATED})
        return Response({'errors': serializer.errors, 'success': False, 'status_code': status.HTTP_400_BAD_REQUEST})