
from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    posts = Post.objects.all()

    # Search posts by title or content
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # Filter posts by category
    if category:
        posts = posts.filter(category__iexact=category)

    return render(
        request,
        'blog/post_list.html',
        {'posts': posts}
    )
