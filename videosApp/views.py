from rest_framework.generics import ListAPIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class VideoView(ListAPIView):
    model = Video
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination 
    queryset = Video.objects.all().order_by('-published_at')