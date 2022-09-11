from rest_framework import generics
from .serializer import CookieSerializer
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly


class CookieList(generics.ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer


class CookieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer
