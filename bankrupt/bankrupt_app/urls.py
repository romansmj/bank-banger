from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('index/', index),
    path('call_me/', call_me),
    path('call_me', call_me),
    path('quiz/', quiz),
    path('quiz', quiz)
]