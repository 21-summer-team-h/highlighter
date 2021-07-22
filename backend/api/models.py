from django.db import models
from django.db import connections

class Video(models.Model):
    video_index = models.AutoField(primary_key=True)
    video_path = models.CharField(max_length=100, blank=True, null=True)
    highlight_count = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'video'


class Highlight(models.Model):
    video_index = models.ForeignKey('Video', models.DO_NOTHING, db_column='video_index', blank=True, null=True)
    highlight_index = models.IntegerField(blank=True, null=True)
    highlight_path = models.CharField(max_length=100, blank=True, null=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    emotion_1 = models.IntegerField(blank=True, null=True)
    emotion_2 = models.IntegerField(blank=True, null=True)
    emotion_3 = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'highlight'
