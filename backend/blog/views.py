from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
# Create your views here.


def index(request):
    return render(request, "index.html")


class BlogListViewApi(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        print(serializer.data)
        resp = {}
        resp['name'] = "Kosgei Victor"

        return Response(serializer._data)
