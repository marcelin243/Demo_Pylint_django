"""
Module de configuration des applications Django pour l'application Exemple.
"""

from django.apps import AppConfig

class ExempleConfig(AppConfig):
    """
    Configuration de l'application Exemple.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exemple'