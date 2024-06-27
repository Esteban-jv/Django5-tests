from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Element
from .forms import ElementForm # With form class
from .forms import ElementModelForm # With form model class


def index(request):
    elements = Element.objects.all()

    paginator = Paginator(elements, 5)
    page_number = request.GET.get('page')
    elements_page = paginator.get_page(page_number)

    return render(request, 'elements/index.html', {'elements': elements_page})

# Create your views here.
def add(request):
    if(request.method == 'POST'):
        form = ElementForm(request.POST)
        # element = form.save()

        if form.is_valid():
            element = Element()
            element.title = form.cleaned_data['title']
            element.slug = form.cleaned_data['slug']
            element.description = form.cleaned_data['description']
            element.price = form.cleaned_data['price']
            element.category = form.cleaned_data['category']
            element.type = form.cleaned_data['type']
            element.save()
            return redirect('element:index')
    else:
        form = ElementForm()

    return render(request, 'elements/add.html', { 'form': form })