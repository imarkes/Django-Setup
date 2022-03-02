from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from backend.core.views import ClienteViewSet, EnderecoViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Setup API",
      default_version='v1',
      description="Api para otimizar o processo de construção de projetos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="i.markes@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],

)


router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'enderecos', EnderecoViewSet, basename='enderecos')

urlpatterns = [
    path("v1/", include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]