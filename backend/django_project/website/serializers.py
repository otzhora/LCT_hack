from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    task = serializers.CharField()
    path = serializers.CharField()
    teacher_id = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
