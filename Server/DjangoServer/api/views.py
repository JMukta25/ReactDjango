from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import UserSerializer, TicketSerializer, userHistorySerializer
from djangoRestApp.models import User, ticket
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
            return Response({"userName" : user.get("userName"), "message":"Valid user"})
        else:
            return Response({"message":"Invalid user"})
    else:
        return Response({"message":"Invalid user"})

@api_view(['GET']) 
def getTicketData(request): 
    tickets = ticket.objects.all() 
    serializer = TicketSerializer(tickets,many = True) 
    return Response(serializer.data) 

@api_view(['POST']) 
def postRequest(request):
    userAction = request.data 
    serializer = userHistorySerializer(data = userAction) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response({"message":"Data inserted"}) 
    else:
        return Response({"message":"Invalid data"})