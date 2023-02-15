from django.shortcuts import render
from .models import Todo ## import Todo model
from rest_framework import viewsets ## class to inherit from
from rest_framework import permissions ## can set permissions for specific routes (ex. only if user is authenticated)
from .serializers import TodoSerializer ## import the serializer we made

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    ## pass the model
    queryset = Todo.objects.all()
    ## pass the serializer
    serializer_class = TodoSerializer
    ## define permissions
    permission_classes = [permissions.AllowAny]
    ## that's it! these lines have created all 5 routes.