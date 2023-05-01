from rest_framework import serializers

from .models import UrlEntity


class RedirectRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlEntity
        fields = ['short_url']


class UrlPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlEntity
        fields = ['long_url']


class UrlResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlEntity
        fields = ['long_url', 'short_url']
