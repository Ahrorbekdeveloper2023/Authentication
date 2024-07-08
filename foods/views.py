from django.shortcuts import render
from .models import FoodType, Food, Comment
from rest_framework.viewsets  import ModelViewSet
from .serializers import FoodSerializer, FoodTypeSerializer, CommentSerializer
from .permissions import FoodTypePermission, FoodPermission, CommentPermission




class FoodTypeViewSet(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [FoodTypePermission]


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [FoodPermission]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]