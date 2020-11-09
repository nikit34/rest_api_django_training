from django.db import models
from django.db.models.signals import pre_save

from restlibrary.utils import unique_slug_generator
from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    slug = models.SlugField(blank=True)
    created = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def product_pre_save_receiver(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Book)