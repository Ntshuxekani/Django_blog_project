from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        Post.objects.create(title=title, content=content, author=author)
        return redirect('home')
    return render(request, 'blog/add_post.html')