from django.forms import ModelForm
from django import forms

from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=('text',)

class OtherWidget(forms.TextInput):
    class Media:
        css = {
            "all" : ["pretty.css"], # could be tv
        }
        js = ["animations.js", "actions.js"]

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            "all" : ["calendar.css"], # could be tv
        }
        js = ["othre.js", "actions.js"]

class CustomTextInput(forms.TextInput):
    icon = ""

    def __init__(self, icon=''):
        self.icon = icon
        super().__init__()
    class Media:
        css = {
            "all" : ["calendar.css"], # could be tv
        }
        js = ["othre.js", "actions.js"]

    def render(self, name, value, attrs=None, renderer=None):
        if self.icon:
            return f'<div class="group"><img src="{self.icon}" alt="">{super().render(name, value, attrs, renderer)}</div>'
        return super().render(name, value, attrs, renderer)

class ContactForm(forms.Form):
    other = forms.CharField(widget=OtherWidget)
    calendar = forms.CharField(widget=CalendarWidget)
    custom = forms.CharField(widget=CustomTextInput)