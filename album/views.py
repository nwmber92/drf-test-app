from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from .models import Album
from .serializers import AlbumSerializer


class AlbumSortingFilter(filters.FilterSet):
    """
    Фильтр, позволяющий выполнять сортировку по текстовому представлению полей модели Album.

    Порядок сортировки определяется значением поля 'sorting' в запросе API.

    Пользователи могут указать порядок сортировки, добавив "-" перед именем поля
    (например, "-year" для сортировки по убыванию).
    """
    sorting = filters.OrderingFilter(
        fields=(
            ('name', 'album'),
            ('year', 'year'),
            ('artist__name', 'artist@name')
        )
    )

    class Meta:
        model = Album
        fields = ['sorting']


class AlbumAPIView(ListAPIView):
    """
    API-представление с простым выводом данных и функционалом сортировки.

    Настройки вывода задаются через параметр ‘REST_FRAMEWORK’ в конфигурации Django.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filterset_class = AlbumSortingFilter
