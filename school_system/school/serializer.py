from rest_framework import serializers
from school.models import School, Student


class SchoolSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=20)


class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, allow_blank=False, max_length=20)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=20)
    school = SchoolSerializer(required=True)
