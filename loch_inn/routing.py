""" from django.urls import path , include
from loch_inn.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
] """
from django.urls import path
from loch_inn.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]