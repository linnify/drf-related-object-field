from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.fields import Field, empty


class DefaultPrimaryKeyField(Field):
    def __init__(self, read_only=False, write_only=False,
                 required=None, default=empty, initial=empty, source=None,
                 label=None, help_text=None, style=None,
                 error_messages=None, validators=None, allow_null=False,
                 serializer_class=None):
        super(DefaultPrimaryKeyField, self).__init__(
            read_only=read_only,
            write_only=write_only,
            required=required,
            default=default,
            initial=initial,
            source=source,
            label=label,
            help_text=help_text,
            style=style,
            error_messages=error_messages,
            validators=validators,
            allow_null=allow_null,
        )
        self.serializer_class = serializer_class

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        if self.serializer_class is not None:
            serializer = self.serializer_class(instance=value)
            return serializer.data
        return value.pk


class ExtendedPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        serializer_class = kwargs.pop("serializer_class", None)
        if "pk_field" not in kwargs.keys():
            kwargs["pk_field"] = DefaultPrimaryKeyField(serializer_class=serializer_class)
        super(ExtendedPrimaryKeyRelatedField, self).__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(value)
        return value.pk
