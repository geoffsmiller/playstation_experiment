from django.contrib import admin
from episodes.models import Series, Episode, Segment, Source


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    fields = ("name", "description", "logo")
    list_display = ("name", "description")


class SegmentInlineAdmin(admin.TabularInline):
    model = Segment
    fields = ("title", "game", "segment_type", "order", "start_time")


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    inlines = [SegmentInlineAdmin]
    fields = ("series", "name", "release_date", "description", "youtube_link")
    list_display = ("name", "series", "release_date")


class SourceInlineAdmin(admin.TabularInline):
    model = Source


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    inlines = [SourceInlineAdmin]
    list_display = ("title", "segment_type", "game", "episode")
