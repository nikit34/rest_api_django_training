from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework.authtoken import views

from .router import *


urlpatterns = [
    path('api/', include(urlpatterns)),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
