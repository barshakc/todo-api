from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from app.models import ToDo
from .serializers import ToDoSerializer

class ToDoAPIView(APIView):
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