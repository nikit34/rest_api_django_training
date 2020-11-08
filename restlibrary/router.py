from rest_framework import routers

from snippets.api.viewsets import SnippetViewSet


router = routers.DefaultRouter()
router.register('snippets', SnippetViewSet, basename='snippet')
