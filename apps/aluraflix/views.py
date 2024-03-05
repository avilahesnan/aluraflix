from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.aluraflix.serializer import ProgramSerializer
from apps.aluraflix.models import Program


class ProgramsViewSet(viewsets.ModelViewSet):
    '''
    View all Programs.

    Returns:
        List of all programs.
    '''

    queryset = Program.objects.all().order_by('title')
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]  # noqa: E501
    ordering_fields = ['title']
    search_fields = ['title']
    filterset_fields = ['type']
