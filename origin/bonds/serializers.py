import requests
from bonds.models import Bonds
from django.conf import settings
from rest_framework import serializers


class BondSerializer(serializers.ModelSerializer):

    legal_name = serializers.SerializerMethodField()

    @staticmethod
    def get_legal_name(obj):

        # Fetch lei record
        response = requests.get(settings.LEI_LOOKUP_URL, params={"lei": obj.lei})

        # Check response code - just in case..
        if response.status_code != 200:
            error = response.json()
            raise serializers.ValidationError("leirecords api returned bad response status code: {} with message: {}"
                                              .format(response.status_code, error["message"]))

        # Transform to json - should be safe at this point
        data = response.json()

        # Cover cases with status 200 but empty lei matches
        if len(data) == 0:
            raise serializers.ValidationError("Lei was not found in leirecords api")

        # Remove spaces (exist in response)
        legal = data[0]["Entity"]["LegalName"]["$"].replace(" ", "")

        return legal

    def list(self, validated_data):
        pass

    def create(self, validated_data):

        new_bond = Bonds.objects.create(**validated_data)
        return new_bond

    class Meta:
        model = Bonds
        exclude = ("id", "owner")
