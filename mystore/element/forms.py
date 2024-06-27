from django import forms
from .models import Category, Element, Type

# deprecated
class ElementForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200, min_length=3)
    slug = forms.SlugField(label='Slug', max_length=200, min_length=3)
    description = forms.CharField(label='Description', widget=forms.Textarea, initial="Xd...")
    price = forms.DecimalField(label='Price', decimal_places=2, max_digits=5, required=False)
    type = forms.ModelChoiceField(label="Type", queryset=Type.objects.all(), initial=1)
    category = forms.ModelChoiceField(label="Category", queryset=Category.objects.all(), initial=1)

class ElementModelForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('title','slug','description','price','type','category')