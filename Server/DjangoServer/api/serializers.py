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
    class Meta: 
        model = userHistory 
        fields = '__all__'  
