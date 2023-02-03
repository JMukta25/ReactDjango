from rest_framework import serializers
from djangoRestApp.models import User, ticket, userHistory
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ticket 
        fields = '__all__' 



class userHistorySerializer(serializers.ModelSerializer): 
    ticket_name = serializers.ReadOnlyField(source = "ticket.ticket_name")
    class Meta: 
        model = userHistory 
        fields = ('status','ticket_name','userName','text')

class storeUserHistorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = userHistory 
        fields = '__all__'