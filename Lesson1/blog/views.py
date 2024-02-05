from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet

from .models import Post, Shop
from .serializers import PostSerializer, ShopSerializer
from rest_framework import viewsets
from rest_framework import generics, mixins, views
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        context = super(PostViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class ShopViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
