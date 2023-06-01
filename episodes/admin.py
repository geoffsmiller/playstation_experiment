from django.contrib import admin
from episodes.models import Series, Episode, Segment, Source


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    fields = ("name", "description", "logo", "order")
    list_display = ("name", "description")


class SegmentInlineAdmin(admin.TabularInline):
    model = Segment
    fields = ("order", "segment_type", "start_time", "short_title")
    readonly_fields = ("short_title",)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    inlines = [SegmentInlineAdmin]
    fields = (
        "series",
        "name",
        "release_date",
        "coverage_start_date",
        "coverage_end_date",
        "description",
        "youtube_link",
        "supplemental_playlist_link",
        "thumbnail_image",
    )
    list_display = ("name", "series", "release_date")


class SourceInlineAdmin(admin.TabularInline):
    model = Source
    fields = ("order", "source_type", "description", "link")


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    inlines = [SourceInlineAdmin]
    list_display = ("title", "segment_type", "episode")
