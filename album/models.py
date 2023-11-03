from django.db import models


class Artist(models.Model):
    """
    Модель, представляющая исполнителя музыкального трека.
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Album(models.Model):
    """
    Модель, представляющая музыкальный альбом.
    """
    name = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name}[{self.year}]"


class Track(models.Model):
    """
    Модель, представляющая музыкальный трек.
    """
    name = models.CharField(max_length=150)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
