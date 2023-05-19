from games.models import Game, GameRelease, GameCompany, GamePlatform, GameRegion
from rest_framework import serializers
from episodes.serializers import SegmentSerializer


class GameRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRegion
        fields = (
            "id",
            "name",
            "flag",
        )


class GamePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlatform
        fields = (
            "id",
            "name",
        )


class GameCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCompany
        fields = (
            "id",
            "name",
        )


class GameReleaseSerializer(serializers.ModelSerializer):
    developers = GameCompanySerializer(many=True)
    publisher = GameCompanySerializer()
    platform = GamePlatformSerializer()
    region = GameRegionSerializer()

    class Meta:
        model = GameRelease
        fields = (
            "id",
            "name",
            "serial_number",
            "release_date",
            "release_date_string",
            "region",
            "platform",
            "developers",
            "publisher",
            "cover_art",
            "cover_art_source_name",
            "cover_art_source_link",
        )


class GameSerializer(serializers.ModelSerializer):
    segment = SegmentSerializer()
    releases = GameReleaseSerializer(many=True)

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
            "releases",
            "segment",
            "cover_art_source_name",
            "cover_art_source_link",
        )
