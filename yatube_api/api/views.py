from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import GenericViewSet

from api.permission import IsOwnerOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Group, Post


class PostViewSet(ListModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  RetrieveModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ListModelMixin,
                     CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def post_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.post_queryset().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.post_queryset()
        )


class GroupViewSet(RetrieveModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class FollowViewSet(ListModelMixin,
                    CreateModelMixin,
                    GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
