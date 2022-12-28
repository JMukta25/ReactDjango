from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import UserSerializer
from djangoRestApp.models import User
from django.http import JsonResponse
@api_view(['POST'])
def registerUser(request):
    user = request.data 
    serializer = UserSerializer(data = user) 
    if serializer.is_valid():
        serializer.save() 
    return Response("User created!!")


@api_view(['POST'])
def loginUser(request):
    user = request.data 
    if User.objects.filter(userName = user.get("userName")):
        valid_user = User.objects.get(userName = user.get("userName"))
        if valid_user and valid_user.passWord == user.get("passWord"):
           

            serializer = UserSerializer(data = valid_user).data
            return JsonResponse(serializer,safe=False)
        else:
            return Response("Invalid credentials")
    else:
        return Response("Invalid credentials!!")