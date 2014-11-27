from django.views.generic import ListView
from .models import Posts

class base_view(ListView):
    queryset = Posts.objects.all().order_by('-created_at')
    context_object_name = 'posts_all'
    template_name = 'base_view.html'