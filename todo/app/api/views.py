from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
# Create your views here.
from app.models import ToDo
from .serializers import ToDoSerializer,UserSerializer
from django.contrib.auth.models import User


class UserRegistration(APIView):

    def post(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
           return Response({'status':403,'error':serializer.errors,'message':'Credentials are invalid'})
        
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj, _=Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':serializer.data,'token':str(token_obj)})


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'status': 200, 'payload': serializer.data, 'token': str(token.key)})
        

class ToDoAPIListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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