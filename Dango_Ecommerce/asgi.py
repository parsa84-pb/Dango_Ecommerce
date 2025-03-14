import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import eshop_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dango_Ecommerce.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            eshop_chat.routing.websocket_urlpatterns
        )
    ),

})
