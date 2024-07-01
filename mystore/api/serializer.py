from rest_framework import serializers

from element.models import Element, Category, Type
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField() # Métodos personalizados para la serialización (Como computed)

    class Meta:
        model = Comment
        fields = '__all__'

    # Useless example
    def get_count(self, obj): # Metodos personalizados para la serialización (paso 2)
        print (obj) # El método se llama get_[nombre del atributo computado] en este caso get_count
        return Comment.objects.filter(element_id=obj.element_id).count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ElementReadOnlySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True) #y así hacemos uso de esa relación inversa declarada en comments.models.py
    class Meta:
        model = Element
        fields = '__all__'
class ElementCreateUpdateDestroySerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # type = TypeSerializer(read_only=True)
    class Meta:
        model = Element
        fields = '__all__'