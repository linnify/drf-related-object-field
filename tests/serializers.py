from rest_framework import serializers

from drf_related_object_field import mixins

from . import models


class AuthorBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("id", "name",)


class BookBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ("id", "title", "year")


class AuthorSerializer(mixins.RelatedObjectFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("id", "name", "books")
        extra_kwargs = {
            "books": {"serializer_class": BookBaseSerializer}
        }


class BookSerializer(mixins.RelatedObjectFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ("id", "title", "year", "author")
        extra_kwargs = {
            "author": {"serializer_class": AuthorBaseSerializer}
        }
