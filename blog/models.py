from django.conf import settings
from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=50, default='null')
    img = models.ImageField(null=True, blank=True, upload_to="projects/")
    img_link = models.CharField(max_length=100, default='null')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    related_language = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
