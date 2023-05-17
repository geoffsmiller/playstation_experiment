import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import mark_safe


class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)
    description = models.TextField()
    logo = models.FileField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "series"

    @property
    def logo_image_tag(self):
        if self.logo:
            return mark_safe(
                '<img src="{base_url}/{bucket_name}/{image_name}" />'
            ).format(
                base_url=settings.IMAGES_BASE_URL,
                bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
                image_name=self.image.name,
            )

    def __str__(self):
        return self.name


class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    series = models.ForeignKey(
        Series, on_delete=models.PROTECT, related_name="episodes"
    )
    name = models.CharField(max_length=1028)
    release_date = models.DateField()
    description = models.TextField()
    youtube_link = models.URLField()
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=False
    )
    supplemental_playlist = models.URLField()

    class Meta:
        ordering = ["series", "order"]

    def __str__(self):
        return f"{self.series}: {self.name}"


class Segment(models.Model):
    SEGMENT_TYPES = [
        ("OP", "Opening"),
        ("Intro", "Intro"),
        ("Feature", "Feature"),
        ("Review", "Review"),
        ("Outro", "Outro"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    episode = models.ForeignKey(
        Episode, on_delete=models.PROTECT, related_name="segments"
    )
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    game = models.ForeignKey(
        "games.Game",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="segments",
    )
    segment_type = models.CharField(max_length=128, choices=SEGMENT_TYPES)
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=False
    )
    start_time = models.CharField(max_length=128)

    class Meta:
        ordering = [
            models.F("episode__series").asc(),
            models.F("episode__order"),
            "order",
        ]


class Source(models.Model):
    SOURCE_TYPE = [("Audio", "Audio"), ("Video", "Video"), ("Image", "Image")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    segment = models.ForeignKey(
        Segment, on_delete=models.PROTECT, related_name="sources"
    )
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=False
    )
    description = models.CharField(max_length=1028)
    link = models.URLField()
