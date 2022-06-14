from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .serializer import *
from .models import Profile


class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet,):

    queryset = Profile.objects.all()
    serializer_class = CreateUserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return UpdateUserSerializer
        elif self.action == 'list':
            return UserListSerializer
        elif self.action == 'retrieve':
            return UserRetrieveSerializer
        elif self.action == 'destroy':
            return UserRetrieveSerializer

    @action(detail=False, methods=['post', ])
    def login_user(self, a):
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(self.request, user)
        token = Token.objects.create(user=user)
        return Response({"Token": token.key}, status=200)

