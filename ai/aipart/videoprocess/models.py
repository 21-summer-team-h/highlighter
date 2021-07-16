from django.db import models
from django.db import connections

class Video(models.Model):
    video_index = models.IntegerField(max_length=)
    video_name = models.CharField(max_length=)
    video_size = models.CharField(max_length=)
    video_time = models.CharField(max_length=)
    video_format = models.CharField(max_length=)
    video_path = models.CharField(max_length=)

    class Meta:
        managed = False
        db_table = 'Video'

class Address(models.Model):
    video_index = models.IntegerField(max_length=)
    highlight_index = model.CharField(max_length=)
    highlight_path = model.CharField(max_length=)
    start = model.CharField(max_length=)
    end = model.CharField(max_length=)
    emotion_1 = model.IntegerField(max_length=)
    emotion_2 = model.IntegerField(max_length=)
    emotion_3 = model.IntegerField(max_length=)

    class Meta:
        managed = False
        db_table = 'Address'