from . import fields


class RelatedObjectFieldMixin(object):
    serializer_related_field = fields.ExtendedPrimaryKeyRelatedField
