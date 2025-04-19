from django.views import generic
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetails(generic.DetailView):
    model = Post
    template_name = 'post_details.html'