from games.models import Game
from games.serializers import GameSerializer
from rest_framework import viewsets


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
