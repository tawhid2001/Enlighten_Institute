from rest_framework import serializers
from . import models

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = '__all__'

class CourseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseResult
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']