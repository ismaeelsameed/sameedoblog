from django.shortcuts import render
from main.models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'main/post_list.html', {'posts': posts})