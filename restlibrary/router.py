from rest_framework_nested import routers
from django.conf.urls import include
from django.urls import path

from authors.api.viewsets import AuthorViewSet, StatisticViewSet
from books.api.viewsets import BookViewSet
from tags.api.viewsets import TagViewSet


base_router = routers.DefaultRouter()
base_router.register('authors', AuthorViewSet)

authors_router = routers.NestedSimpleRouter(base_router, 'authors', lookup='author')
authors_router.register('books', BookViewSet)
authors_router.register('statistic', StatisticViewSet)

books_router = routers.NestedSimpleRouter(authors_router, 'books', lookup='book')
books_router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(base_router.urls)),
    path('', include(authors_router.urls)),
    path('', include(books_router.urls)),
]