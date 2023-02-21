from django.urls import path
from app.consumers import NotificationConsumer

websocket_urlpatterns =[

    path('ws/wsc/',NotificationConsumer.as_asgi())
]