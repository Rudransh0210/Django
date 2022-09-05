from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.db import models
from .models import backend

class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = backend
        fields = '__all__'

    def create(self, validated_data):
        x=backend.objects.create(
            name=validated_data['name'],
            title=validated_data['title'],
            content=validated_data['content']
        )
        backend.save(x)
        return x

