from django.db import models


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=20,)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    slug = models.CharField(max_length=100, unique=True, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ', slug: ' + self.slug
