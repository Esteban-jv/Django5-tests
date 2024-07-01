from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from element.models import Element, Category, Type
from comments.models import Comment
from .serializer import CommentSerializer, ElementReadOnlySerializer, ElementCreateUpdateDestroySerializer, CategorySerializer, TypeSerializer

class CreateUpdateDestroyViewSet(mixins.CreateModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    pass
class ElementReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Element.objects.all()
    serializer_class = ElementReadOnlySerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Element.objects.all()
        serializer = ElementReadOnlySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def url(self, request):
        print(request.query_params['slug'])
        queryset = Element.objects.get(slug=request.query_params['slug'])

        serializer = ElementReadOnlySerializer(queryset, many=False)
        return Response(serializer.data)

class ElementCreateUpdateDestroyViewSet(CreateUpdateDestroyViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementCreateUpdateDestroySerializer

    def perform_create(self, seriaizer):
        print("Preform create")
        super().perform_create(seriaizer)
        # catid = self.request.data.get("category")
        # typeid = self.request.data.get("type_id")
        # seriaizer.save(
        #     category=Category.objects.get(pk=catid),
        #     type=Category.objects.get(pk=typeid)
        # )


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
'''


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def url(self, request):
        queryset = get_object_or_404(Category, slug=request.query_params['slug'])

        serializer = CategorySerializer(queryset, many=False)
        return Response(serializer.data)

class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(type_id=pk)
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Type.objects.all()
        serializer = TypeSerializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def url(self, request):
        queryset = get_object_or_404(Type, slug=request.query_params['slug'])
        serializer = TypeSerializer(queryset, many=False)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.exclude(element__isnull=True)
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
'''