from rest_framework import serializers
from notes.models import Program

class ProgramSerializiers(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['programTitle']