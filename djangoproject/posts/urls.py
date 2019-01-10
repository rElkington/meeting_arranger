from django.urls import path
from posts.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]