from django.conf import settings
from django.db import models
from django.utils import timezone

# Models created below.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_published = models.DateField(null=True,blank=True)


    def publish(self):
        self.date_published = timezone.now().date()
        self.save()

    def __str__(self):
        return self.title
