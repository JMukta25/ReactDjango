from django.urls import path 
from . import views
urlpatterns = [
    path('registerUser/',views.registerUser), 
    path('loginUser/',views.loginUser),
    path('getTicketData',views.getTicketData),
    path('postRequest/',views.postRequest),
    path('userInfo/<str:username>/',views.getUserInfo),
    path('getTicketInfo/<int:id>/',views.getTicketInfo),
]
