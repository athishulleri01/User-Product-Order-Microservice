from django.apps import AppConfig
# from .consumers import start_user_check_consumer

class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    # def ready(self):
    #     start_user_check_consumer()