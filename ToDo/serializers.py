from rest_framework import serializers
from ToDo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'text',
        )
        model = models.ToDoItem