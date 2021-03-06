from django.db import models
from django.db.models.signals import pre_save

from books.models import Book
from restlibrary.utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def tag_pre_save_reciever(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_reciever, sender=Tag)