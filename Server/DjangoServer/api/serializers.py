from rest_framework import serializers
from djangoRestApp.models import User 
from djangoRestApp.models import ticket 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ticket 
        fields = '__all__' 