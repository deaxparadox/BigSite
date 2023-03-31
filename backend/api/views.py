from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from extras.models import india


def states_list(request):
    if request.method == "GET":
        states = india.State.objects.all()
        serializer = serializers.StateSerializer(states, many=True)
        return JsonResponse(serializer.data, safe=False)

