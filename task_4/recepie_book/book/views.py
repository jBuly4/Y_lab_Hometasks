from django.shortcuts import render
from django.views.generic import ListView, DetailView

from book.models import Post

# Create your views here.

class List_of_Posts_View(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get('slug'))


class Detail_View_of_Post(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request, 'base.html')
