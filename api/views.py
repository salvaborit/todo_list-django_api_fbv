from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Task
from base.models import Label
from .serializers import TaskSerializer
from .serializers import LabelSerializer


@api_view(['GET'])
def api_status(request):
    return Response({'status': 'OK'})


@api_view(['GET', 'POST'])
def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_labels(request):
    if request.method == 'GET':
        labels = Label.objects.all()
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

        # @api_view(['GET'])
        # def get_tasks_by_label(request):
        #     pass

        # @api_view(['GET'])
        # def get_tasks(request):
        #     START USING ORM
