from episodes.models import Episode, Series
from episodes.serializers import EpisodeSerializer, SeriesSerializer
from rest_framework import viewsets


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SeriesSerializer
    queryset = Series.objects.all()


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
