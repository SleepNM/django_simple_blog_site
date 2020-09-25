from django.shortcuts import render
from .models import Blog


def home(request):
    blogs = Blog.objects.all().order_by('-time')
    return render(request, 'home.html', {'blogs': blogs})


def blog(request):
    if request.method == "POST":
        author = request.POST["username"]
        if author == "":
            author = 'Annonimus'
        data = Blog(
            author=author.capitalize(),
            title=request.POST["blogname"].title(),
            content=request.POST["content"],
            slug=request.POST["blogname"].replace(" ", "-").lower()
        )
        data.save()
        return render(request, 'blog.html', {'posted': True})
    else:
        return render(request, 'blog.html')


def blogpost(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogpost.html', {'blog': blog})
