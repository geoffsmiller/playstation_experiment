from games.models import Game
from rest_framework import serializers
from episodes.serializers import SegmentSerializer


class GameSerializer(serializers.ModelSerializer):
    segment = SegmentSerializer()

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
            "segment",
        )
