from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    born = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
