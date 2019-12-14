from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

from .serializers import LikeSerializer, CommentSerializer
from webapp.models import Like, Comment, Image


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def create(self, request, *args, **kwargs):
        pk = request.data.get('photo')
        photo = Image.objects.get(pk=pk)
        # print(pk,photo)
        # print(self.queryset.filter(photo=photo))
        if self.queryset.filter(photo=photo):
            return Response({'error': 'You have already liked it'}, status=400)
        photo.likenum += 1
        photo.save()
        return super(LikeViewSet, self).create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = request.data.get('photo')
        photo = Image.objects.get(pk=pk)
        if not self.queryset.filter(photo=photo):
            return Response({'error': 'No likes yet'}, status=400)
        photo.likenum -= 1
        photo.save()
        return super(LikeViewSet, self).create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
          return [AllowAny()]

        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return [DjangoModelPermissions()]