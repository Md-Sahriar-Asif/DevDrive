from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = [
        ("FRONTEND", "Frontend"),
        ("BACKEND", "Backend"),
        ("FULLSTACK", "Fullstack"),
        ("ML", "Machine Learning"),
        ("DL", "Deep Learning"),
        ("AI", "Artificial Intelligence"),
        ("LLM", "Large Language Models"),
        ("CYBER", "Cyber Security"),
        ("SWE", "Software Engineering"),
    ]
    title = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=1000)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to="img/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs')

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body
