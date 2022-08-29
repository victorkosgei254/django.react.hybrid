from django.db import models

# Create your models here.


class Blog(models.Model):
    blogTitle = models.CharField(max_length=300)
    blogBody = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.blogTitle
