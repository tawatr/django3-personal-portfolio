from django.shortcuts import render, get_object_or_404
from .models import myBlog

# Create your views here.
def all_blogs(request):
    # import all attributes of model
    # and turn to python object
    #blog = myBlog.objects.order_by('-date')[:5]
    # If we want to limit to first five entries.
    blog = myBlog.objects.order_by('-date')[:5]
    return render( request,'myblog/all_blogs.html',
    {'blogs':blog} )

def detail(request, blog_id):
    # To get particular blog object
    blog=get_object_or_404(myBlog, pk=blog_id)
    # pk is database term
    return render(
    request, 'myblog/detail.html',
    {'blog_id':blog_id, 'blog':blog})
