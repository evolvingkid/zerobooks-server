from django.shortcuts import render
from django.http import JsonResponse

from notes.serializers import ProgramSerializiers
from notes.models import Program

# Create your views here.

# to get all programs / classes in the database
def program(request):
    programs = Program.objects.all()
    serializer = ProgramSerializiers(programs, many=True)
    return JsonResponse(serializer.data, safe=False)

