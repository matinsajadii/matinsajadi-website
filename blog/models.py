from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    content = models.TextField()
    slug = models.SlugField()
    author = models.CharField(max_length=80)
    reading_time = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="image_blog")


    def __str__(self):
        return  self.title
