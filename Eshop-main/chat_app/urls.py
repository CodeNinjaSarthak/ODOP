from django.urls import path
from . import views

urlpatterns = [
    path("ask", views.chat, name="chat"),
    path("ask_question/", views.ask_question, name="ask_question"),
]
