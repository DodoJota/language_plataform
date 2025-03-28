from django.apps import AppConfig


class LanguageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'language'

    def ready(self):
        import language.signals