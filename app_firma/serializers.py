from rest_framework import serializers
from urllib3.util import Url

from app_firma.models import Title, Result, Letters, Search, Absolute


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = ['letter_name', 'select_letter']


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'


class AbsoluteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absolute
        fields = '__all__'


