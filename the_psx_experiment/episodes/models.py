import uuid

from django.db import models

class Episode(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4. editable=False)
    order = models.IntegerField()
    release_date = models.DateField()


class EpisodeSegment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.IntegerField()
    episode = models.ForeignKey(Episode, on_delete=models.PROTECT, related_name='segments')
    title = models.CharField(max_length=512)
