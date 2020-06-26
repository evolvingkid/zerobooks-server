from django.shortcuts import render
from django.http import JsonResponse

from notes.serializers import *
from notes.models import *

# Create your views here.

# to get all programs / classes in the database
def program(request):
    programs = Program.objects.all()
    serializer = ProgramSerializiers(programs, many=True)
    return JsonResponse(serializer.data, safe=False)

# to get all course / subject in the database
def course(request):
    course = Course.objects.all()
    serializer = CourseSerializiers(course, many=True)
    return JsonResponse(serializer.data, safe=False)
