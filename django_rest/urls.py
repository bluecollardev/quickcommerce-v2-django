"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .router import router

from rest_framework_swagger.views import get_swagger_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_swagger_view(title='QuickCommerce-API')

schema_view1 = get_schema_view(
   openapi.Info(
      title="QuickCommerce API",
      default_version='v1',
      description="Test Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@bluecollardev.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/', schema_view),
    path('swagger.json', schema_view1.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
