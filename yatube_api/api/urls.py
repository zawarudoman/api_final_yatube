from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

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

urlpatterns_ver1 = [
    path('', include(router_ver1.urls)),
]

urlpatterns_jwt = [
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(urlpatterns_ver1)),
    path('v1/', include(urlpatterns_jwt)),
]
