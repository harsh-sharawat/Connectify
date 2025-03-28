from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    # re_path(r"/feed/ws/(?P<room_id>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"^ws/feed/(?P<room_id>\w+)/$", ChatConsumer.as_asgi()),

]