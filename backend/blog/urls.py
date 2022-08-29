from importlib.resources import path
from .views import BlogListViewApi, index

from django.urls import path, include
urlpatterns = [
    path("api/v1/blog", BlogListViewApi.as_view()),
    path("", index, name="index")
]
