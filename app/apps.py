from django.apps import AppConfig
#from channels_redis.core import RedisChannelLayer


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    #CHANNEL_LAYERS = {"default": {"BACKEND": "channels_redis.core.RedisChannelLayer","CONFIG": {"hosts": [("127.0.0.1", 6379)],},},}