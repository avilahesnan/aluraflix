from django.urls import path, include
from rest_framework import routers
from apps.aluraflix.views import ProgramsViewSet


app_name = 'aluraflix'

router = routers.DefaultRouter()

router.register('programs', ProgramsViewSet, basename='Programs')

urlpatterns = [
    path('', include(router.urls)),
]
