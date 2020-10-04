from rest_framework import serializers


class BaseFourWordModelSerializer(serializers.ModelSerializer):
    """Base Model serializer abstract class."""
    pass


class BaseFourWordReadOnlySerializer(serializers.Serializer):
    """Base Model serializer abstract class."""
    pass
