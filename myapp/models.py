from django.utils import timezone
from django.urls import reverse
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=2500)
    posted_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=False)
    
    class Meta:
        ordering = ['posted_date']
    
    def __str__(self):
        return self.title
    