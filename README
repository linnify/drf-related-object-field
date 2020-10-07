# Django REST Framework Related Object Field

A lightweight package that allows for custom handling on `PrimaryKeyRelatedField` in serializers.
The default behaviour of the mixin is to allow the normal behaviour of the `PrimaryKeyRelatedField` for
writes (i.e. require the PK as input data for POST, PUT and PATCH) and to render the related object using
the given serializer for GET requests. If no serializer is passed, defaults to the normal behaviour.

Serialization (i.e. object to data) works in both ways of the relationship, that is you can
simply use the mixin just like in the snippet below. However, for deserialization (i.e. data
to object), this only works (it is only tested) for many to one relationship in this exact direction.
That is, if you have an `Author` and a `Book`, where an author can have many books, then
you will only be able to create/edit the books by passing them the author ID, but not vice-versa.

## Code example

```python
from rest_framework import serializers

from drf_related_object_field.mixins import RelatedObjectFieldMixin

class RelatedObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyRelatedModel
        fields = "__all__"

class MySerializer(RelatedObjectFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ("id", "name", "my_related_object")
        extra_kwargs = {
            "my_related_object": {
                "serializer_class": RelatedObjectSerializer,
            },
        }

```