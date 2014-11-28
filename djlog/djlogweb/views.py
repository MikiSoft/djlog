from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Posts

class base_view(ListView):
    queryset = Posts.objects.all().order_by('-created_at')
    context_object_name = 'posts_all'
    template_name = 'base_view.html'

class post_view(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'post_view.html'