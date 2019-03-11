from rest_framework import serializers

from website import models


class TLESerializer(serializers.ModelSerializer):
    """
    Serializer for TLE instances in the api.
    """
    class Meta:
        model = models.TLE
        fields = ['at', 'lines']


class SatelliteSerializer(serializers.ModelSerializer):
    """
    Serializer for the satellite api.
    """
    class Meta:
        model = models.Satellite
        fields = ['id', 'name', 'norad_id', 'description']


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the location api.
    """
    class Meta:
        model = models.Location
        fields = ['name', 'latitude', 'longitude', 'elevation']
