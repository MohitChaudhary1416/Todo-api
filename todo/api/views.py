from rest_framework.generics import GenericAPIView
from rest_framework import status
from todo.models import Todo
from todo.api.serializer import TodoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class TodoGet(GenericAPIView):

    def get(self,request):
        data = Todo.objects.all()
        serializer = TodoSerializer(data,many = True)
        return Response({
            "Message":"Data Fetch Sucessfully",
            "data":serializer.data
        },status.HTTP_200_OK)
    
class TodoPost(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message":"Content Added Sucessfully",
                "data":serializer.data
            },status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class TodoUpdate(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def put(self,request,todo_id):
        data = request.data
        todo = get_object_or_404(Todo,id = todo_id)
        if not todo_id:
            return Response({
                "Message":"Id didn't found"
            },status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(data=data,instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message":"Content Updated Sucessfully",
                "data":serializer.data
            },status.HTTP_200_OK)
        return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class TodoDelete(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request,todo_id):
        todo = get_object_or_404(Todo,id =todo_id)
        todo.delete()
        return Response({
            "Message":"Content Deleted Sucessfully"
        },status.HTTP_204_NO_CONTENT)



