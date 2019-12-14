from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly

from .serializers import LikeSerializer, CommentSerializer
from webapp.models import Like, Comment


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

