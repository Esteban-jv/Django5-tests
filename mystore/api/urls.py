from django.urls import path
from rest_framework import routers

from .viewset import ElementReadOnlyViewSet, ElementCreateUpdateDestroyViewSet, CategoryViewSet, TypeViewSet, CommentViewSet
from . import views

route = routers.SimpleRouter()

route.register('element-ro', ElementReadOnlyViewSet, basename='element-ro')
route.register('element', ElementCreateUpdateDestroyViewSet, basename='element')
route.register('category', CategoryViewSet)
route.register('type', TypeViewSet)
route.register('comment', CommentViewSet)

urlpatterns = route.urls

urlpatterns.append(path('login',views.login))