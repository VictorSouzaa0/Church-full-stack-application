from rest_framework import serializers
from .models import Archdiocese, People, Role, Church


class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'role_name',
            'responsible'
        ]

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = [
            'id',
            'name',
            'age'
        ]


class ChurchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = [
            'id',
            'church_name',
            'address',
            'fk_people'
        ]


class ArchdioceseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Archdiocese
        fields = [
            'id',
            'fk_people',
            'location',
            'fk_church'
        ]