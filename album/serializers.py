from rest_framework import serializers
from collections import OrderedDict

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Album
    """
    album = serializers.SerializerMethodField()
    tracks = serializers.StringRelatedField(many=True, read_only=True)
    artist_name = serializers.CharField(source='artist.name', read_only=True)

    def get_album(self, obj):
        """
        Возвращает строковое представление альбома.
        """
        return str(obj)

    def to_representation(self, instance):
        """
        Переопределяет родительский метод.
        Изменяет представление исполнителя в ответе API
        и формирует упорядоченный список полей для вывода.
        """
        representation = super().to_representation(instance)
        representation['artist@name'] = instance.artist.name
        ordered_representation = OrderedDict()
        for field in ['album', 'name', 'artist@name', 'tracks']:
            ordered_representation[field] = representation.get(field)
        return ordered_representation

    class Meta:
        model = Album
        fields = ['album', 'name', 'artist_name', 'tracks']
