
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializers
    def get(self,request, format=None):
        """return a list APIView features"""
        api_view=["test is here", "ok i will test you",
        "Hello user test me",
        ]

        return Response({'messages':'Hello','an_apiview':api_view})

    def post(self, request):
        """create  a hello messages with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello{name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put (self,request,pk=None):

        return Response({'method':'PUT'})
        
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

# Create your views here.
