from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import Task
from base.models import Tag
from .serializers import TaskSerializer
from .serializers import TagSerializer


@api_view(['GET'])
def api_status(request, format=None):
    """ route 'status/' """
    return Response({'status': 'OK'})


@api_view(['GET', 'POST'])
def get_tasks(request, format=None):
    """ route 'tasks/' """

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"tasks": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_task_by_id(request, id, format=None):
    """ route 'tasks/<int:id>/' """

    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response({'task': serializer.data})

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'updated task': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_tags(request, format=None):
    """ route 'tags/' """

    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response({"tags": serializer.data})

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"tags": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_tags_by_id(request, id, format=None):
    """ route 'tags/<int:id>/' """

    try:
        tag = Tag.objects.get(pk=id)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response({'tag': serializer.data})

    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'updated task': serializer.data})

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_tasks_by_tag(request, id, format=None):
    """ route 'tags/<int:id>/tasks/' """
    try:
        tag = Tag.objects.get(pk=id)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tasks = Task.objects.filter(tags=tag)
        serializer = TaskSerializer(tasks, many=True)
        # intermediate model of m:m relationship of tasks/tags
        # inter_model = Task.tags.through
        # tasks = inter_model.objects.filter(tag=tag)
        # serialize tasks (object type: type of intermediary table)
        return Response({'tasks': serializer.data})
