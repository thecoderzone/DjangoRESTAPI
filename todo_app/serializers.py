from rest_framework import serializers
from .models import todo


class TodoSerializer(serializers.Serializer):
     """Serializes our models"""
     task = serializers.CharField(max_length=150)
     completed = serializers.BooleanField()
     user_id = serializers.IntegerField()
     
     
     def create(self, validated_data):
          """ Create """
          return todo.objects.create(**validated_data)
     
     
     def update(self, instance, validated_data):
          """updating APIView"""
          instance.task = validated_data.get('task', instance.task)
          instance.completed = validated_data.get('complete', instance.completed)
          instance.user_id = validated_data.get('user_id', instance.user_id)
          
          instance.save()
          return instance
          
          