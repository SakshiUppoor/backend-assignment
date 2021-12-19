from django.urls import path
from . import views

urlpatterns = [
    path('',views.VideoView.as_view()),
    path('dashboard',views.dashboard),
]
