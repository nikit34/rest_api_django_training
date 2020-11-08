from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework.authtoken import views

from restlibrary.router import urls


urlpatterns = [
    path('api/', include(('restlibrary.router', ''))),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
