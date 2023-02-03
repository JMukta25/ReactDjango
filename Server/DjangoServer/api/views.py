from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import UserSerializer, TicketSerializer, userHistorySerializer, storeUserHistorySerializer
from djangoRestApp.models import User, ticket, userHistory
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
    serializer = storeUserHistorySerializer(data = userAction)
    if serializer.is_valid(): 
        serializer.save()
        print("checking") 
        return Response({"message":"Data inserted"})
        
    else:
        print(userAction)
        return Response({"message":"Invalid data"})


@api_view(['GET']) 
def getUserInfo(request,username):
    userInfo = userHistory.objects.filter(userName = username)
    serializer = userHistorySerializer(userInfo,many = True) 
    return Response(serializer.data)

@api_view(['GET'])
def getTicketInfo(request,id):
    ticketInfo = ticket.objects.filter(id = id)
    serilizer = TicketSerializer(ticketInfo,many = True)
    return Response(serilizer.data)

