from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post

# Create your views here.

def indexView(request):
    """
    A function based view to show index page
    """
    return render(request, 'index.html')


class IndexView(TemplateView):
    """
    A class based view to show index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context