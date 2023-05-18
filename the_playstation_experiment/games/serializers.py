from games.models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "id",
            "name",
            "release_date",
            "platforms",
            "publishers",
            "developers",
        )
