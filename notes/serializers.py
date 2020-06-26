from rest_framework import serializers
from notes.models import *

# program serializers
class ProgramSerializiers(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


# course serializers
class CourseSerializiers(serializers.ModelSerializer):
    program = ProgramSerializiers(many=False)
    class Meta:
        model = Course
        fields = '__all__'
        
