from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_status(request):
    return Response({'status': 'OK'})

# @api_view(['GET'])
# def get_tasks(request):
#     START USING ORM
