from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from ToDo import models
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = models.ToDoItem.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ToDoItem.objects.all()
    serializer_class = TodoSerializer