from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Video
from .serializers import VideoSerializer
from .utils.custom_paginator import CustomPageNumberPagination
# Create your views here.

class VideoView(ListAPIView):
    model = Video
    serializer_class = VideoSerializer
    pagination_class = CustomPageNumberPagination 
    queryset = Video.objects.all().order_by('-published_at')

def dashboard(request):
    return render(request, 'index.html')