from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.aluraflix.serializer import ProgramSerializer
from apps.aluraflix.models import Program


class ProgramsViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['type']
