from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import ValidationError
from django.utils.text import slugify
from .models import Category, Element, Type

class ElementForm(forms.Form):
    title = forms.CharField(label='Title',
                            max_length=200,
                            min_length=3,
                            validators=[
                                MinLengthValidator(3,
                                                   message='Very short! (min %(limit_value)d current %(show_value)d)'
                                                   )
                            ],
                            widget=forms.TextInput(
                                attrs= {
                                    'class': 'form-control',
                                    'data-id': '50'
                                }
                            ))
    slug = forms.SlugField(label='Slug', max_length=200, min_length=3)
    description = forms.CharField(label='Description', widget=forms.Textarea, initial="Xd...")
    price = forms.DecimalField(label='Price', decimal_places=2, max_digits=5, required=False)
    type = forms.ModelChoiceField(label="Type", queryset=Type.objects.all(), initial=1)
    category = forms.ModelChoiceField(label="Category", queryset=Category.objects.all(), initial=1) #, widget=forms.RadioSelect)

    #Custom validations for specific field [title] (This may not be a good example)
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Element.objects.filter(title=title).exists():
    #         raise ValidationError('Title already exists')
    #     return title

    #Custom validation for all fields
    # def clean(self):
    #     form_data = self.cleaned_data
    #     if form_data['slug'] != slugify(form_data['title']):
    #         self._errors['slug'] = ['Slug do not match title']
    #         del form_data['slug']
    #     return form_data

# deprecated
class ElementModelForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('title','slug','description','price','type','category')