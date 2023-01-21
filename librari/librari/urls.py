"""librari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import AuthorModelViewSet, ArticleModelViewSet, BookModelViewSet, BiographyModelViewSet, MyAPIView
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('my', MyAPIView, basename='my')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token)
    # path('myapi/', MyAPIView.as_view({'get': 'list'})),
]
