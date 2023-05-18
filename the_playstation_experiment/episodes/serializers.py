from episodes.models import Episode, Segment, Series
from rest_framework import serializers


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("id", "name", "description", "logo")


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = "__all__"


class EpisodeSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    segments = SegmentSerializer(many=True)

    class Meta:
        model = Episode
        fields = (
            "id",
            "name",
            "description",
            "release_date",
            "coverage_date_span",
            "order",
            "supplemental_playlist",
            "series",
            "segments",
        )
