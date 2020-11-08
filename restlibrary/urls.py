from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework.authtoken import views
from .router import router


urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
