import uuid

from django.db import models


class GameMeta(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class GameRegion(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64, unique=True)
    earliest_release_date = models.DateField()
    
    class Meta():
        ordering = ['code']
    
    def __str__(self):
        return f'{self.name}({self.code})'


class GameRelease(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512)
    region = models.ForeignKey(GameRegion, on_delete=models.PROTECT)
    release_date = models.DateField()


class GameDisc(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=512)
    release = models.ForeignKey(GameRelease, on_delete=models.PROTECT, related_name='discs')

    class Meta():
        ordering = ['serial']

    def __str__(self):
        return f'{self.serial} - {self.title}'
