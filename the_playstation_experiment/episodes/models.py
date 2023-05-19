import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import mark_safe


class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1028)
    description = models.TextField()
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=False
    )
    logo = models.FileField()

    class Meta:
        ordering = ["order"]
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
    release_date = models.DateField(null=True, blank=False)
    coverage_start_date = models.DateField(null=True, blank=False)
    coverage_end_date = models.DateField(null=True, blank=False)
    description = models.TextField()
    youtube_link = models.URLField()
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=False
    )
    supplemental_playlist_link = models.URLField()
    thumbnail_image = models.FileField(null=True)

    class Meta:
        ordering = ["series", "order"]

    @property
    def coverage_date_span_string(self):
        if self.coverage_start_date == self.coverage_end_date:
            return f"{self.coverage_start_date.strftime('%B %-d, %Y')}"
        return f"{self.coverage_start_date.strftime('%B %-d, %Y')} to {self.coverage_end_date.strftime('%B %-d, %Y')}"

    @property
    def release_date_string(self):
        return f"{self.release_date.strftime('%B %-d, %Y')}"

    def __str__(self):
        return f"{self.series}: {self.name}"


class Segment(models.Model):
    SEGMENT_TYPES = [
        ("OP", "Opening"),
        ("Intro", "Intro"),
        ("Feature", "Feature"),
        ("Review", "Review"),
        ("Chapter", "Chapter"),
        ("Release Roundup", "Release Roundup"),
        ("Outro", "Outro"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    episode = models.ForeignKey(
        Episode, on_delete=models.PROTECT, related_name="segments"
    )
    feature_name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
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

    @property
    def short_title(self):
        if self.segment_type == "Review":
            return f"Review: {self.games.first()}"
        elif self.segment_type == "Feature":
            return f"Feature: {self.feature_name}"
        else:
            return f"{self.segment_type}"

    @property
    def title(self):
        return f"{self.episode} | {self.short_title}"

    @property
    def start_time_seconds(self):
        seconds = 0
        split_start_time = self.start_time.split(":")
        if len(split_start_time) == 3:
            seconds += int(split_start_time.pop(0)) * 60 * 60
        seconds += int(split_start_time.pop(0)) * 60
        seconds += int(split_start_time.pop(0))
        return f"{seconds}s"

    @property
    def youtube_link(self):
        return f"{self.episode.youtube_link}&t={self.start_time_seconds}"

    def __str__(self):
        return f"{self.title}"


class Source(models.Model):
    SOURCE_TYPE = [
        ("Audio", "Audio"),
        ("Video", "Video"),
        ("Image", "Image"),
        ("Research", "Research"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    segment = models.ForeignKey(
        Segment, on_delete=models.PROTECT, related_name="sources"
    )
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=False
    )
    source_type = models.CharField(
        max_length=128, choices=SOURCE_TYPE, null=True, blank=False
    )
    description = models.CharField(max_length=1028)
    link = models.URLField()
