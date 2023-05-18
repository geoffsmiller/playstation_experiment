from rest_framework import serializers

from episodes.models import Episode, Segment, Series, Source


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("id", "name", "description", "logo")


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class SegmentSerializer(serializers.ModelSerializer):
    sources = SourceSerializer(many=True)

    class Meta:
        model = Segment
        fields = (
            "id",
            "title",
            "short_title",
            "description",
            "start_time",
            "youtube_link",
            "sources",
        )


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
            "youtube_link",
            "supplemental_playlist",
            "series",
            "segments",
        )
