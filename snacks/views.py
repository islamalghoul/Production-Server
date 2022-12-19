from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import SnackSerializer
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
# Create your views here.
from .models import Snack


class SnackListView(ListCreateAPIView):
    queryset=Snack.objects.all()
    serializer_class= SnackSerializer
    permission_classes=[IsOwnerOrReadOnly]


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Snack.objects.all()
    serializer_class= SnackSerializer
    permission_classes=[IsOwnerOrReadOnly]