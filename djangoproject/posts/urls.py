from django.urls import path
from posts.views import HomeView, YesView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login', LoginView.as_view(template_name='posts/loginIndex.html'), name='loginIndex'),
     path('yes', YesView.as_view(), name='confirm_attendance'),
]