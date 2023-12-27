from apps.todos.models import Todos
from rest_framework import serializers


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        exclude = ['user_id', 'important', 'is_completed', 'created_at', 'updated_at']


class TodosRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        exclude = ['user_id', 'created_at', 'updated_at']


class TodosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        exclude = ['user_id', 'is_completed', 'created_at', 'updated_at']


class TodosUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        exclude = ['user_id', 'created_at', 'updated_at']
