from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_ver1 = DefaultRouter()
router_ver1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router_ver1.register('follow', FollowViewSet, basename='follow')
router_ver1.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
router_ver1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('v1/', include(router_ver1.urls)),
    path('v1/', include('djoser.urls.jwt')),

]
