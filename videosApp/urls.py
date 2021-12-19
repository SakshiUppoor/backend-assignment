from django.urls import path
from . import views

urlpatterns = [
    path('api/list',views.VideoView.as_view()),
    path('dashboard',views.dashboard),
]
