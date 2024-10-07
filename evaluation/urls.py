from django.urls import path
from .infrastructure.views import EvaluationView

urlpatterns = [
    path('evaluate/', EvaluationView.as_view(), name='evaluate'),
]