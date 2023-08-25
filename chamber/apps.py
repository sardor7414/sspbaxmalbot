from django.apps import AppConfig


class ChamberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chamber'

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"