from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField()
    created = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
