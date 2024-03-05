from django.urls import path, include
from rest_framework import routers
from apps.aluraflix.views import ProgramsViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Aluraflix API",
      default_version='v1',
      description="Local provider of series and movies developed by Alura in the course of Django Rest",  # noqa: E501
      terms_of_service="#",
      contact=openapi.Contact(email="contact@aluraflix.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'aluraflix'

router = routers.DefaultRouter()

router.register('programs', ProgramsViewSet, basename='Programs')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa: E501
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa: E501
]
