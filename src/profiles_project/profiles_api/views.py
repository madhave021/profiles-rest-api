from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from  .  import permissions
from . import serializers

from . import models

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):

        an_apiview= [
        'Uses HTTP methods as function (get, post, patch, delete,put)',
        'Is similiar to a traditional Django view',
        'Gives you the most control over ypur logic',
        'Is mapped mannualy to urls',

        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello{0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(request,self,pk=None):

        return Response({'method' : 'put'})


    def patch(request,self,pk=None):

        return Response({'method': 'patch'})

    def delete (request,self,pk=None):
         return Response({'method': 'delete'})
class HelloViewSet(viewsets.ViewSet):
    serializer_class= serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles deleting an object."""

        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes= (permissions.UpdateOwnProfile,)
