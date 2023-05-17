import uuid

from django.db import models


class GamePlatform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)

    def __str__(self):
        return self.name


class GameCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)

    class Meta:
        verbose_name_plural = "game companies"

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)

    @property
    def release_date(self):
        pass


class GameRelease(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    serial_number = models.CharField(max_length=1028)
    release_date = models.DateField()
    region = models.CharField(max_length=1028)
    platform = models.ForeignKey(
        GamePlatform, on_delete=models.PROTECT, related_name="games"
    )
    developer = models.ForeignKey(
        GameCompany, on_delete=models.PROTECT, related_name="developed_games"
    )
    publisher = models.ForeignKey(
        GameCompany, on_delete=models.PROTECT, related_name="published_games"
    )