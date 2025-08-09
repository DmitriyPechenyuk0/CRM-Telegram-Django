from django.urls import path
from .views import RenderHome

urlpatterns = [
    path('', view=RenderHome.as_view(), name='home')
]
