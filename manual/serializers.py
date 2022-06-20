from rest_framework import serializers

from manual.models import ManualElem, ManualVersion


class ManualElemSerializer(serializers.ModelSerializer):
    """
    Serializer for ManualElem model
    """

    class Meta:
        model = ManualElem
        fields = '__all__'
        depth = 2


class ManualVersionSerializer(serializers.ModelSerializer):
    """
    Serializer for ManualVersion model
    """
    class Meta:
        model = ManualVersion
        fields = ('id', 'manual_info', 'version', 'from_date')
        depth = 1
