from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework_nested import routers

from snippets.api.viewsets import SnippetViewSet
from authors.api.viewsets import AuthorViewSet
from books.api.viewsets import BookViewSet
from tags.api.viewsets import TagViewSet


base_router = routers.DefaultRouter()
base_router.register('authors', AuthorViewSet)

authors_router = routers.NestedSimpleRouter(base_router, 'authors', lookup='author')
authors_router.register('books', BookViewSet)

books_router = routers.NestedSimpleRouter(authors_router, 'books', lookup='book')
books_router.register('tags', TagViewSet)


urlpatterns = [
    path('authors', base_router.urls),
    path('books', authors_router.urls),
    path('tags', books_router.urls),
]