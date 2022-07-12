from django.core.exceptions import ValidationError
from rest_framework import serializers
from ..utils import nid_validation


class NIDSerializer(serializers.Serializer):
    national_id = serializers.CharField(
        required=True, validators=[nid_validation])
