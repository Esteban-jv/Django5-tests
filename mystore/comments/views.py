from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Comment
from .forms import CommentForm

# Create your views here.
# def add(request):
#     if(request.method == 'GET'):
#         return render(request, 'comments/add.html')
#     elif(request.method == 'POST'):
#         if request.POST.get('comments') != '':
#             print(request)
#             comment = Comment()
#             comment.text = request.POST.get('comments')
#             comment.save()
#         else:
#             print("Comment is null")
#
#     return render(request, 'comments/add.html')

def add(request):
    if(request.method == 'POST'):
        form = CommentForm(request.POST)
        comment = form.save()
        return redirect('comments:index')
    else:
        form = CommentForm()

    return render(request, 'comments/add.html', { 'form': form })

def index(request):
    comments = Comment.objects.all()

    paginator = Paginator(comments, 2)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)

    return render(request, 'comments/index.html', {'comments': comments_page})

def update(request, id):
    comment = get_object_or_404(Comment, pk=id)
    # try:
    #     comment = Comment.objects.get(pk=id)
    # except Comment.DoesNotExist:
    #     raise Http404

    if (request.method == 'POST'):
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comments:index')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/add.html', {'form': form})

def delete(request, id):
    comment = Comment.objects.get(id=id)

    if request.method == 'POST':
        comment.delete()
        return redirect('comments:index')

