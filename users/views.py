from django.shortcuts import render
from rest_framework.generics import ListAPIView

from users.models import User
from users.serializers import UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
