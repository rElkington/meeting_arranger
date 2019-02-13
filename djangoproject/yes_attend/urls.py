from django.urls import path
from yes_attend.views import YesView

urlpatterns = [
    path('', YesView.as_view(), name='index'),
]