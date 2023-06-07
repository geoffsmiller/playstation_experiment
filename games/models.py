import uuid

from django.db import models


class GameRegion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    flag = models.FileField()

    def __str__(self):
        return self.name


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


class GameRelease(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)
    game = models.ForeignKey(
        "games.Game", on_delete=models.CASCADE, related_name="releases"
    )
    serial_number = models.CharField(max_length=1028)
    release_date = models.DateField()
    approximate_release_date = models.CharField(max_length=1028, null=True, blank=True)
    region = models.ForeignKey(
        GameRegion, on_delete=models.PROTECT, related_name="games", null=True
    )
    platform = models.ForeignKey(
        GamePlatform, on_delete=models.PROTECT, related_name="games"
    )
    developers = models.ManyToManyField(GameCompany, related_name="developed_games")
    publisher = models.ForeignKey(
        GameCompany, on_delete=models.PROTECT, related_name="published_games"
    )
    cover_art = models.FileField(null=True, blank=True)
    cover_art_source_name = models.CharField(max_length=1028, null=True, blank=True)
    cover_art_source_link = models.URLField(null=True, blank=True)
    is_master_release = models.BooleanField(default=False)
    is_master_cover_art = models.BooleanField(default=False)

    class Meta:
        ordering = ["release_date", "-is_master_release"]

    @property
    def release_date_string(self):
        if self.approximate_release_date:
            return self.approximate_release_date
        else:
            return self.release_date.strftime("%B %-d, %Y")


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)
    segment = models.ForeignKey(
        "episodes.Segment",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="games",
    )

    class Meta:
        ordering = ["name"]

    @property
    def cover_art(self):
        cover_art = None
        if self.releases.filter(is_master_cover_art=True).exists():
            cover_art = self.releases.filter(is_master_cover_art=True).first().cover_art
        elif self.releases.filter(is_master_release=True).exists():
            cover_art = self.releases.filter(is_master_release=True).first().cover_art
        if cover_art:
            return cover_art.url

    @property
    def cover_art_source_name(self):
        if self.releases.filter(is_master_cover_art=True).exists():
            return (
                self.releases.filter(is_master_cover_art=True)
                .first()
                .cover_art_source_name
            )
        elif self.releases.filter(is_master_release=True).exists():
            return (
                self.releases.filter(is_master_release=True)
                .first()
                .cover_art_source_name
            )

    @property
    def cover_art_source_link(self):
        if self.releases.filter(is_master_cover_art=True).exists():
            return (
                self.releases.filter(is_master_cover_art=True)
                .first()
                .cover_art_source_link
            )
        elif self.releases.filter(is_master_release=True).exists():
            return (
                self.releases.filter(is_master_release=True)
                .first()
                .cover_art_source_link
            )

    @property
    def release_date(self):
        release_date = "Unknown"
        if self.releases.count():
            if self.releases.filter(is_master_release=True).exists():
                release_date = (
                    self.releases.filter(is_master_release=True)
                    .first()
                    .release_date.strftime("%B %-d, %Y")
                )
            else:
                release_date = (
                    self.releases.order_by("release_date")
                    .first()
                    .release_date.strftime("%B %-d, %Y")
                )
        return release_date

    @property
    def platforms(self):
        platforms = set()
        for release in self.releases.all():
            platforms.add(release.platform.name)
        return ", ".join(sorted(platforms))

    @property
    def publishers(self):
        publishers = set()
        for release in self.releases.all():
            publishers.add(release.publisher.name)
        return ", ".join(sorted(publishers))

    @property
    def developers(self):
        developers = set()
        for release in self.releases.all():
            for developer in release.developers.all():
                developers.add(developer.name)
        return ", ".join(sorted(developers))

    def __str__(self):
        return self.name
