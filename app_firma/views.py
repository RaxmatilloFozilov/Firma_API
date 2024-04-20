from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from app_firma.models import Title, Result, Search, Letters, Absolute
from app_firma.permissions import MyPermission
from app_firma.serializers import (
    TitleSerializer,
    ResultSerializer,
    SearchSerializer,
    LettersSerializer,
    AbsoluteSerializer
)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [MyPermission]


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [MyPermission]


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = [MyPermission]


class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer
    permission_classes = [MyPermission]


class AbsoluteViewSet(viewsets.ModelViewSet):
    queryset = Absolute.objects.all()
    serializer_class = AbsoluteSerializer
    permission_classes = [MyPermission]

    def get_queryset(self):
        if self.action == 'GET' and 'id' in self.kwargs:
            return AbsoluteSerializer
        return AbsoluteSerializer

