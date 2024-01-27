from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
from app.models import ToDo
from .serializers import ToDoSerializer

class ToDoAPIListView(ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer

    def get(self, request, *args, **kwargs):
       todos = self.queryset.all()
       serializer = self.serializer_class(todos, many=True)
       return Response(serializer.data)

    def post(self,request,*args,**kwargs):
      serializer = self.serializer_class(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ToDoAPIDetailView(APIView):
  queryset=ToDo.objects.all()
  serializer_class=ToDoSerializer
  
  def get(self,request,*args,**kwargs):
      todo = ToDo.objects.get(pk=kwargs['pk'])
      serializer = ToDoSerializer(todo)
      return Response(serializer.data)
   
  def put(self, request, *args, **kwargs):
      instance = self.queryset.get(pk=kwargs['pk'])
      serializer = self.serializer_class(instance, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def patch(self, request, *args, **kwargs):
      instance = self.queryset.get(pk=kwargs['pk'])
      serializer = self.serializer_class(instance, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,*args,**kwargs):
     instance = get_object_or_404(self.queryset, pk=kwargs['pk'])
     instance.delete()
     return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)