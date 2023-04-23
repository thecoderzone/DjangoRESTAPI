from django.shortcuts import render

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from . models import todo
from . serializers import TodoSerializer


# Create your views here.

class TodolistApi(APIView):
     
     # add permission to check if user is authenticated
     permission_classes = [permissions.IsAuthenticated]
     
     
     # Get 
     def get(self, request):
          """
          Get all objects
          """
          todos = todo.objects.all()
          serializer = TodoSerializer(todos, many=True)
          
          return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
     
     
     # Post 
     def post(self, request):
          """
          Creates an object
          """
         
          list = {
                   "task":request.data.get('task'),
                   "completed":request.data.get('completed'),
                   "user_id": request.user.id
          } 
          
          # Creating a todo from the above data
          serializer = TodoSerializer(data = list)
          if serializer.is_valid(raise_exception=True):
               serializer.save()
               
               return Response(serializer.data, status=status.HTTP_201_CREATED)
           
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
     
class TodoDetailApi(APIView):
     """
     Creating Patch request and a delete
     """
     
     # add permission to check if user is authenticated
     permission_classes = [permissions.IsAuthenticated]
     

     def get_object(self, todo_id, user_id):
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            return todo.objects.get(id=todo_id, user = user_id)
        except todo.DoesNotExist:
            return None
          
     def get(self, request, todo_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK) 
   
     def put(self, request, todo_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
            
        list = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user_id': request.user.id
        }
        serializer = TodoSerializer(instance = todo_instance, data=list, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
    
     def delete(self, request, todo_id):
        """ 
        Delete a todo list
        """
        
        todo_instance = self.get_object(todo_id, request.user.id)
        
        if not todo_instance:
            return Response({"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        todo_instance.delete()
            
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)