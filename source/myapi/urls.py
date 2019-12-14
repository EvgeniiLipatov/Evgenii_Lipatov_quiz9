from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)


app_name = 'myapi'

urlpatterns = [
    path('', include(router.urls)),

]