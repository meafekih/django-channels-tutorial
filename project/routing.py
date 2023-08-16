from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from app import consumers
from django.core.asgi import get_asgi_application


# urls that handles the websocket connection is put here
websocket_urlpatterns=[
                    re_path(
                        r"ws/chat/(?P<chat_box_name>\w+)/$", consumers.ChatRoomConsumer.as_asgi()
                    ),
                ]

application = ProtocolTypeRouter( 
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)
