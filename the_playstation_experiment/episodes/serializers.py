from rest_framework import serializers

from episodes.models import Episode, Segment, Series, Source
from games.models import Game


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("id", "name", "description", "logo")


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class NestedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "id",
            "name",
            "release_date",
            "platforms",
            "publishers",
            "developers",
            "cover_art",
        )


class NestedEpisodeSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()

    class Meta:
        model = Episode
        fields = (
            "id",
            "name",
            "series",
        )


class SegmentSerializer(serializers.ModelSerializer):
    sources = SourceSerializer(many=True)
    games = NestedGameSerializer(many=True)
    episode = NestedEpisodeSerializer()

    class Meta:
        model = Segment
        fields = (
            "id",
            "segment_type",
            "title",
            "short_title",
            "description",
            "start_time",
            "youtube_link",
            "sources",
            "games",
            "episode",
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
            "release_date_string",
            "coverage_date_span_string",
            "order",
            "youtube_link",
            "supplemental_playlist_link",
            "series",
            "segments",
            "thumbnail_image",
        )
